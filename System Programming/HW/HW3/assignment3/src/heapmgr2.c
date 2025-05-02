/*--------------------------------------------------------------------*/
/* heapmgr2.c                                                         */
/* Author: 2023-12753 EunSu Yeo                                       */
/*--------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include "chunk.h"

#define FALSE 0
#define TRUE  1

// Configuration constants
enum {
    MEMALLOC_MIN = 1024,
    NUM_BINS     = 128,     
    BIN_UNIT     = 64       
};

// Global heap state
// Array of free-list heads per bin
static Chunk_T g_free_bins[NUM_BINS];   
static void   *g_heap_start = NULL;     
static void   *g_heap_end   = NULL;     

// Static helper function declarations
static void   init_my_heap(void);
static size_t size_to_units(size_t size);
static int    get_bin_index(size_t units);
static Chunk_T get_chunk_from_data_ptr(void *m);
static void   insert_chunk(Chunk_T c);
static void   remove_chunk(Chunk_T c);
static void   merge_chunk(Chunk_T c);
#ifndef NDEBUG
static int    check_heap_validity(void);
#endif

/*--------------------------------------------------------------------*/
/* init_my_heap:                                                      */
/*   Initialize the managed heap region by capturing the current      */
/*   program break.  Zero out all bin heads.                          */
/*--------------------------------------------------------------------*/
static void
init_my_heap(void)
{
    g_heap_start = g_heap_end = sbrk(0);
    if (g_heap_start == (void *)-1) {
        fprintf(stderr, "sbrk(0) failed\n");
        exit(EXIT_FAILURE);
    }
    // Initialize free bins to NULL
    for (int i = 0; i < NUM_BINS; i++) {
        g_free_bins[i] = NULL;
    }
}

/*--------------------------------------------------------------------*/
/* size_to_units:                                                     */
/*   Convert a requested payload size in bytes to chunk units needed, */
/*   including header and footer overhead, rounded up to CHUNK_UNIT.   */
/*--------------------------------------------------------------------*/
static size_t
size_to_units(size_t size)
{
    // total size = size + header + footer
    // header and footer are needed so +2 is added 
    size_t total_size = size + 2 * sizeof(struct Chunk);
    return (total_size + (CHUNK_UNIT - 1)) / CHUNK_UNIT;
}

/*--------------------------------------------------------------------*/
/* get_bin_index:                                                     */
/*   Compute appropriate bin index for a chunk of given size units.   */
/*   Sizes above last bin map into the highest bin.                   */
/*--------------------------------------------------------------------*/
static int
get_bin_index(size_t units)
{
    // index = (size / BIN_UNIT) 
    // if the index is bigger than the last bin, set it to the last bin
    int idx = (int)((units * CHUNK_UNIT) / BIN_UNIT);
    if (idx >= NUM_BINS) idx = NUM_BINS - 1;
    return idx;
}

/*--------------------------------------------------------------------*/
/* get_chunk_from_data_ptr:                                           */
/*   Translate a user pointer returned by heapmgr_malloc to its chunk */
/*   header pointer.                                                  */
/*--------------------------------------------------------------------*/
static Chunk_T
get_chunk_from_data_ptr(void *m)
{
    // m points to the user data area
    // Then we need to subtract the size of the header to get the pointer of header
    return (Chunk_T)((char *)m - sizeof(struct Chunk));
}

/*--------------------------------------------------------------------*/
/* insert_chunk:                                                      */
/*   Place a free chunk into the head of its bin list (LIFO).         */
/*   Sets status to FREE, updates prev/next pointers, and writes footer. */
/*--------------------------------------------------------------------*/
static void
insert_chunk(Chunk_T c)
{   
    // set the status of chunk to free
    chunk_set_status(c, CHUNK_FREE);
    // set index of the chunk
    int idx = get_bin_index(chunk_get_units(c));
    // link to the free list
    // c->free_ptr = g_free_bins[idx];
    chunk_set_next_free(c, g_free_bins[idx]);
    // set the previous free chunk pointer to NULL
    chunk_set_prev_free(c, NULL);
    // set c's footer to point the previous free chunk
    if (g_free_bins[idx]) {
        chunk_set_prev_free(g_free_bins[idx], c);
    }
    // set free list head to the new chunk
    // which will work as stack
    g_free_bins[idx] = c;
    // set the footer of the chunk
    chunk_set_footer(c);
}

/*--------------------------------------------------------------------*/
/* remove_chunk:                                                      */
/*   Remove a chunk from its bin free-list.  Fix neighbor pointers.   */
/*   Does not change chunk status.                                    */
/*--------------------------------------------------------------------*/
static void
remove_chunk(Chunk_T c)
{
    // get the index of the chunk
    // work same as the heapmgr1.c
    int idx = get_bin_index(chunk_get_units(c));
    Chunk_T prev = chunk_get_prev_free(c);
    Chunk_T next = chunk_get_next_free(c);
    // if there is a previous free chunk
    // set the next free chunk pointer of the previous chunk to the next chunk
    if (prev) {
        chunk_set_next_free(prev, next);
    } 
    else {
        g_free_bins[idx] = next;
    }
    // if there is a next free chunk
    // set the previous free chunk pointer of the next chunk to the previous chunk
    if (next) {
        chunk_set_prev_free(next, prev);
    }
    /*
    inital state: prev <--> c <--> next 
    next state: prev --> next | prev <-- c  <-- next
    final state: prev <--> next
    */
}

/*--------------------------------------------------------------------*/
/* merge_chunk:                                                       */
/*   Merge adjacent free chunks (prev and next) around 'c'.  After    */
/*   coalescing, reinsert the combined chunk into appropriate bin.    */
/*--------------------------------------------------------------------*/
static void
merge_chunk(Chunk_T c)
{
    /* Attempt to merge with previous chunk */
    // work same as the heapmgr1.c
    Chunk_T prev = chunk_get_prev_adjacent(c, g_heap_start, g_heap_end);
    if (prev && chunk_get_status(prev) == CHUNK_FREE) {
        // remove the previous chunk from the free list
        remove_chunk(prev);
        // combine two chunks like the previous one
        chunk_set_units(prev, chunk_get_units(prev) + chunk_get_units(c));
        chunk_set_footer(prev);
        // set the chunk to the previous chunk
        c = prev;
    }

    /* Attempt to merge with next chunk */
    Chunk_T next = chunk_get_next_adjacent(c, g_heap_start, g_heap_end);
    // check if the next chunk is in free list
    if (next && chunk_get_status(next) == CHUNK_FREE) {
        remove_chunk(next);
        // combine two chunks like the previous one
        chunk_set_units(c, chunk_get_units(c) + chunk_get_units(next));
        chunk_set_footer(c);
    }

    /* Reinsert coalesced chunk */
    insert_chunk(c);
}

#ifndef NDEBUG
/*--------------------------------------------------------------------*/
/* check_heap_validity:                                               */
/*   Verify that all bins' free lists are internally consistent and   */
/*   chunks are within heap bounds and marked free.                  */
/*--------------------------------------------------------------------*/
static int 
check_heap_validity(void)
{
    Chunk_T c, next_free, prev_free, adj;
    /* 1. Verify heap boundaries */
    if (g_heap_start == NULL) {
        fprintf(stderr, "Uninitialized heap start\n");
        return FALSE;
    }
    if (g_heap_end == NULL) {
        fprintf(stderr, "Uninitialized heap end\n");
        return FALSE;
    }
    /* 2. If heap is empty, all bins must be empty */
    if (g_heap_start == g_heap_end) {
        for (int i = 0; i < NUM_BINS; i++) {
            if (g_free_bins[i] != NULL) {
                fprintf(stderr, "Non-empty bin on zero-size heap\n");
                return FALSE;
            }
        }
        return TRUE;
    }
    /* 3. Traverse entire heap region and validate each chunk */
    for (c = (Chunk_T)g_heap_start;
        c != NULL && (void*)c < g_heap_end;
        c = chunk_get_next_adjacent(c, g_heap_start, g_heap_end)) {
        if (!chunk_is_valid(c, g_heap_start, g_heap_end)) {
            fprintf(stderr, "Invalid chunk\n");
            return FALSE;
        }
    }
    /* 4. Check each bin's free-list integrity */
    for (int i = 0; i < NUM_BINS; i++) {
        prev_free = NULL;
        for (c = g_free_bins[i]; c != NULL; c = next_free) {
            next_free = chunk_get_next_free(c);
            /* a) Status must be FREE and chunk valid */
            if (chunk_get_status(c) != CHUNK_FREE) {
                fprintf(stderr, "Non-free chunk in bin \n");
                return FALSE;
            }
            if (!chunk_is_valid(c, g_heap_start, g_heap_end)) {
                fprintf(stderr, "Invalid free chunk in bin \n");
                return FALSE;
            }
            /* b) prev_free pointer consistency */
            if (chunk_get_prev_free(c) != prev_free) {
                fprintf(stderr, "prev_free mismatch in bin \n");
                return FALSE;
            }
            /* c) No uncoalesced adjacent free chunks */
            adj = chunk_get_next_adjacent(c, g_heap_start, g_heap_end);
            if (adj != NULL && chunk_get_status(adj) == CHUNK_FREE) {
                fprintf(stderr, "Uncoalesced free chunks\n");
                return FALSE;
            }
            prev_free = c;
        }
    }
    return TRUE;
}
#endif

/*--------------------------------------------------------------------*/
/* heapmgr_malloc:                                                    */
/*   Allocate 'size' bytes.  Search bins starting at target size bin, */
/*   splitting chunks if possible.  If no chunk found, extend heap.   */
/*--------------------------------------------------------------------*/
void *
heapmgr_malloc(size_t size)
{
    static int initialized = FALSE;
    if (size == 0) return NULL;
    if (!initialized) {
        // Initialize the heap
        init_my_heap();
        initialized = TRUE;
    }
    assert(check_heap_validity());

    // get the exact size of the chunk in units
    size_t units = size_to_units(size);
    // get the bin index of the chunk
    int    start = get_bin_index(units);

    /* Search for fit in bins */
    // search the bins starting from index from 0
    for (int i = start; i < NUM_BINS; i++) {
        for (Chunk_T c = g_free_bins[i]; c; c = chunk_get_next_free(c)) {
            if (chunk_get_units(c) >= units) {
                remove_chunk(c);
                // header and footer are needed so +2 is added in back
                if (chunk_get_units(c) > units + 2) {
                    Chunk_T split = (Chunk_T)((char *)c + units * CHUNK_UNIT);
                    // set the size of the new chunk to the remaining size
                    // size of c - unit = size of split
                    chunk_set_units(split, chunk_get_units(c) - units);
                    chunk_set_status(split, CHUNK_FREE);
                    chunk_set_footer(split);
                    insert_chunk(split);
                    chunk_set_units(c, units);
                }
                // change state to used state
                chunk_set_status(c, CHUNK_IN_USE);
                chunk_set_footer(c);
                assert(check_heap_validity());
                return (char *)c + sizeof(struct Chunk);
            }
        }
    }

    /* No fit: extend heap */
    // same as heapmgr1.c
    size_t req = units * CHUNK_UNIT;
    Chunk_T nc = (Chunk_T)sbrk(req);
    if (nc == (Chunk_T)-1) return NULL;
    g_heap_end = sbrk(0);

    chunk_set_units(nc, units);
    chunk_set_status(nc, CHUNK_FREE);
    chunk_set_footer(nc);
    insert_chunk(nc);
    return heapmgr_malloc(size);
}

/*--------------------------------------------------------------------*/
/* heapmgr_free:                                                      */
/*   Free a previously allocated block and coalesce neighbors.        */
/*--------------------------------------------------------------------*/
void
heapmgr_free(void *m)
{
    // check if the pointer is NULL
    if (!m) return;
    assert(check_heap_validity());

    // get the chunk header from the user pointer
    Chunk_T c = get_chunk_from_data_ptr(m);
    assert(chunk_get_status(c) == CHUNK_IN_USE);

    // set the status of the chunk to free
    chunk_set_status(c, CHUNK_FREE);
    // set the footer of the chunk
    chunk_set_footer(c);
    // merge the chunk with its neighbors if possible
    merge_chunk(c);

    assert(check_heap_validity());
}
