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
    MEMALLOC_MIN = 4096,    
    NUM_BINS     = 10,     
    BIN_UNIT     = 64       
};

// Global heap state
static Chunk_T g_free_bins[NUM_BINS];   /* Array of free-list heads per bin */
static void   *g_heap_start = NULL;     
static void   *g_heap_end   = NULL;     

// Static helper function declarations
static void   init_my_heap(void);
static size_t size_to_units(size_t size);
static int    get_bin_index(size_t units);
static Chunk_T get_chunk_from_data_ptr(void *m);
static void   insert_chunk(Chunk_T c);
static void   remove_chunk(Chunk_T c);
static void   coalesce_chunk(Chunk_T c);
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
    size_t total = size + 2 * sizeof(struct Chunk);
    return (total + (CHUNK_UNIT - 1)) / CHUNK_UNIT;
}

/*--------------------------------------------------------------------*/
/* get_bin_index:                                                     */
/*   Compute appropriate bin index for a chunk of given size units.   */
/*   Sizes above last bin map into the highest bin.                   */
/*--------------------------------------------------------------------*/
static int
get_bin_index(size_t units)
{
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
    chunk_set_status(c, CHUNK_FREE);
    int idx = get_bin_index(chunk_get_units(c));
    chunk_set_next_free(c, g_free_bins[idx]);
    chunk_set_prev_free(c, NULL);
    if (g_free_bins[idx]) {
        chunk_set_prev_free(g_free_bins[idx], c);
    }
    g_free_bins[idx] = c;
    chunk_set_footer(c);
}

/*--------------------------------------------------------------------*/
/* remove_chunk:                                                      */
/*   Remove a chunk from its bin free-list.  Fix up neighbor pointers.*/
/*   Does not change chunk status.                                    */
/*--------------------------------------------------------------------*/
static void
remove_chunk(Chunk_T c)
{
    int idx = get_bin_index(chunk_get_units(c));
    Chunk_T prev = chunk_get_prev_free(c);
    Chunk_T next = chunk_get_next_free(c);
    if (prev) {
        chunk_set_next_free(prev, next);
    } else {
        g_free_bins[idx] = next;
    }
    if (next) {
        chunk_set_prev_free(next, prev);
    }
}

/*--------------------------------------------------------------------*/
/* coalesce_chunk:                                                    */
/*   Merge adjacent free chunks (prev and next) around 'c'.  After    */
/*   coalescing, reinsert the combined chunk into appropriate bin.    */
/*--------------------------------------------------------------------*/
static void
coalesce_chunk(Chunk_T c)
{
    /* Attempt to merge with previous chunk */
    if ((char *)c > (char *)g_heap_start) {
        Chunk_T prev_footer = (Chunk_T)((char *)c - sizeof(struct Chunk));
        size_t prev_units = prev_footer->size_status >> 1;
        Chunk_T prev = (Chunk_T)((char *)c - prev_units * CHUNK_UNIT);
        if (prev && chunk_get_status(prev) == CHUNK_FREE) {
            remove_chunk(prev);
            chunk_set_units(prev,
                chunk_get_units(prev) + chunk_get_units(c));
            chunk_set_footer(prev);
            c = prev;
        }
    }

    /* Attempt to merge with next chunk */
    Chunk_T next = chunk_get_next_adjacent(c, g_heap_start, g_heap_end);
    if (next && chunk_get_status(next) == CHUNK_FREE) {
        remove_chunk(next);
        chunk_set_units(c,
            chunk_get_units(c) + chunk_get_units(next));
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
    for (int i = 0; i < NUM_BINS; i++) {
        for (Chunk_T c = g_free_bins[i]; c; c = chunk_get_next_free(c)) {
            if (!chunk_is_valid(c, g_heap_start, g_heap_end))
                return FALSE;
            if (chunk_get_status(c) != CHUNK_FREE)
                return FALSE;
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
        init_my_heap();
        initialized = TRUE;
    }
    assert(check_heap_validity());

    size_t units = size_to_units(size);
    int    start = get_bin_index(units);

    /* Search for fit in bins */
    for (int i = start; i < NUM_BINS; i++) {
        for (Chunk_T c = g_free_bins[i]; c; c = chunk_get_next_free(c)) {
            if (chunk_get_units(c) >= units) {
                remove_chunk(c);
                /* Split if large enough */
                if (chunk_get_units(c) > units + 2) {
                    Chunk_T split = (Chunk_T)((char *)c + units * CHUNK_UNIT);
                    chunk_set_units(split,
                        chunk_get_units(c) - units);
                    chunk_set_status(split, CHUNK_FREE);
                    chunk_set_footer(split);
                    insert_chunk(split);
                    chunk_set_units(c, units);
                }
                chunk_set_status(c, CHUNK_IN_USE);
                chunk_set_footer(c);
                assert(check_heap_validity());
                return (char *)c + sizeof(struct Chunk);
            }
        }
    }

    /* No fit: extend heap */
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
    if (!m) return;
    assert(check_heap_validity());

    Chunk_T c = get_chunk_from_data_ptr(m);
    assert(chunk_get_status(c) == CHUNK_IN_USE);

    chunk_set_status(c, CHUNK_FREE);
    chunk_set_footer(c);
    coalesce_chunk(c);

    assert(check_heap_validity());
}
