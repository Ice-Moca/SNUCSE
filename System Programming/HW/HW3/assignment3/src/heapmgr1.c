/*--------------------------------------------------------------------*/
/* heapmgr1.c                                                         */
/* Author: 2023-12753 EunSu Yeo                                       */
/*--------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include "chunk.h"

#define FALSE 0
#define TRUE  1

enum { MEMALLOC_MIN = 1024 };

/* g_free_head: point to first chunk in the free list */
static Chunk_T g_free_head = NULL;

/* g_heap_start, g_heap_end: start and end of the heap area.
 * g_heap_end will move if you increase the heap */
static void *g_heap_start = NULL, *g_heap_end = NULL;

#ifndef NDEBUG
/* check_heap_validity:
 * Validity check for entire data structures for chunks. Note that this
 * is basic sanity check, and passing this test does not guarantee the
 * integrity of your code. 
 * Returns 1 on success or 0 (zero) on failure. 
 */
/* Updated check_heap_validity for heapmgrbase.c with link checks */
static int
check_heap_validity(void)
{
    Chunk_T c, next_free, prev_free;

    /* Case 1: Verify heap boundaries */
    if (g_heap_start == NULL) {
        fprintf(stderr, "Uninitialized heap start\n");
        return FALSE;
    }
    if (g_heap_end == NULL) {
        fprintf(stderr, "Uninitialized heap end\n");
        return FALSE;
    }

    /* Case 2: If heap is empty, free list must be empty */
    if (g_heap_start == g_heap_end) {
        if (g_free_head == NULL) {
            return TRUE;
        }
        fprintf(stderr, "Inconsistent empty heap\n");
        return FALSE;
    }

    /* Case 3: Traverse entire heap region and validate each chunk */
    for (c = (Chunk_T)g_heap_start;
        c != NULL && (void *)c < g_heap_end;
        c = chunk_get_next_adjacent(c, g_heap_start, g_heap_end)) {
        if (!chunk_is_valid(c, g_heap_start, g_heap_end)) {
            fprintf(stderr, "Invalid chunk\n");
            return FALSE;
        }
    }

    /* Case 4: Check free-list about the status, linkage, and merging */
    prev_free = NULL;
    for (c = g_free_head; c != NULL; c = next_free) {
        next_free = chunk_get_next_free(c);

        /* a) Must be marked free and valid */
        if (chunk_get_status(c) != CHUNK_FREE) {
            fprintf(stderr, "Non-free chunk in free list\n");
            return FALSE;
        }
        if (!chunk_is_valid(c, g_heap_start, g_heap_end)) {
            fprintf(stderr, "Invalid free chunk\n");
            return FALSE;
        }

        /* b) prev_free pointer consistency */
        if (chunk_get_prev_free(c) != prev_free) {
            fprintf(stderr, "prev_free mismatch\n");
            return FALSE;
        }

        /* c) No adjacent unmerged free chunks */
        Chunk_T adj = chunk_get_next_adjacent(c, g_heap_start, g_heap_end);
        if (adj != NULL && adj == next_free) {
            fprintf(stderr, "Uncoalesced chunks\n");
            return FALSE;
        }
        prev_free = c;
    }
    return TRUE;
}
#endif

/*--------------------------------------------------------------------*/
/* size_to_units:                                                     
    Convert a byte request size into chunk units, accounting for   
    header and footer overhead.  Rounds up to the nearest unit.      
*/
/*--------------------------------------------------------------------*/
static size_t
size_to_units(size_t size)
{
    // total size = size + header + footer
    size_t total_bytes = size + 2 * sizeof(struct Chunk);
    // to give the size of chunk in units 
    // round up to the nearest 
    // Think of edge case: total bytes = 9
    // In this case 2 size are needed so to make that happen 
    // we need to add 7 to make it 16
    return (total_bytes + (CHUNK_UNIT - 1)) / CHUNK_UNIT;
}

/*--------------------------------------------------------------------*/
/* get_chunk_from_data_ptr:                                           
    Given a pointer returned by heapmgr_malloc, compute the pointer  
    to its Chunk header.                                            
*/
/*--------------------------------------------------------------------*/
static Chunk_T
get_chunk_from_data_ptr(void *m)
{
    // m points to the user data area
    // Then we need to subtract the size of the header to get the pointer of header
    return (Chunk_T)((char *)m - sizeof(struct Chunk));
}

/*--------------------------------------------------------------------*/
/* init_my_heap:                                                      
    Initialize heap boundaries by querying current program break.    
    Sets g_heap_start and g_heap_end to the same address.           
*/
/*--------------------------------------------------------------------*/
static void
init_my_heap(void)
{
    /* Initialize g_heap_start and g_heap_end */
    g_heap_start = g_heap_end = sbrk(0);
    if (g_heap_start == (void *)-1) {
        fprintf(stderr, "sbrk(0) failed\n");
        exit(EXIT_FAILURE);
    }
}

/*--------------------------------------------------------------------*/
/* insert_chunk:                                                      */
/*   Insert free chunk c at the head of the free list.                */
/*   Marks the chunk as free, sets next/prev pointers, and writes     */
/*   the footer.                                                      */
/*--------------------------------------------------------------------*/
static void
insert_chunk(Chunk_T c)
{   
    // make the chunk to free
    chunk_set_status(c, CHUNK_FREE);
    // link into the free list
    // c->free_ptr = g_free_head;
    chunk_set_next_free(c, g_free_head);
    // set the previous free chunk pointer to NULL
    chunk_set_prev_free(c, NULL);
    // set c's footer to point the previous free chunk
    if (g_free_head){
        chunk_set_prev_free(g_free_head, c);
    }
    // set free list head to the new chunk
    // which will work as stack
    g_free_head = c;
    // set the footer of the chunk 
    chunk_set_footer(c);
}

/*--------------------------------------------------------------------*/
/* remove_chunk:                                                      */
/*   Remove chunk c from the free list, fixing up neighbors.          */
/*   Does not change the chunk's in-use/free status.                  */
/*--------------------------------------------------------------------*/
static void
remove_chunk(Chunk_T c)
{
    // get the previous and next free chunk pointers
    Chunk_T prev = chunk_get_prev_free(c);
    Chunk_T next = chunk_get_next_free(c);
    // if there is a previous free chunk
    // set the next free chunk pointer of the previous chunk to the next chunk
    if (prev){
        chunk_set_next_free(prev, next);
    }
    // else set the free list head to the next chunk
    else{
        g_free_head = next;
    }
    // if there is a next free chunk
    // set the previous free chunk pointer of the next chunk to the previous chunk
    if (next){
        chunk_set_prev_free(next, prev);
    }
    /*
    inital state: prev <--> c <--> next 
    next state: prev --> next | prev <-- c  <-- next
    final state: prev <--> next
    */
}

/*--------------------------------------------------------------------*/
/* merge_chunks:                                                     */
/*   Coalesce adjacent free chunks around 'c'.  If the previous or    */
/*   next chunk is free, remove it and absorb its units into 'c'.     */
/*   Returns the pointer to the merged chunk (may differ from input).  */
/*--------------------------------------------------------------------*/
static Chunk_T
merge_chunks(Chunk_T c)
{
    /* Attempt to merge with previous chunk */
    Chunk_T prev = chunk_get_prev_adjacent(c, g_heap_start, g_heap_end);
    // check if the previous chunk is in free list
    if (prev && chunk_get_status(prev) == CHUNK_FREE) {
        remove_chunk(prev);
        // combine two chunks like the next one
        chunk_set_units(prev, chunk_get_units(prev) + chunk_get_units(c));
        chunk_set_footer(prev);
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

    return c;
}

/*--------------------------------------------------------------------*/
/* heapmgr_malloc:                                                    */
/*   Allocate 'size' bytes of memory from the custom heap.            */
/*   Searches the free list for a fit, splits if necessary, and      */
/*   extends the heap with sbrk if no suitable chunk exists.          */
/*   Returns a pointer to the user data area or NULL on failure.     */
/*--------------------------------------------------------------------*/
void *
heapmgr_malloc(size_t size)
{
    static int initialized = FALSE;
    if (size == 0){
        return NULL;
    }
    if (!initialized) {
        // Initialize the heap
        init_my_heap();
        initialized = TRUE;
    }

    assert(check_heap_validity());
    // get the exact size of the chunk in units
    size_t units = size_to_units(size);

    // First-fit search 
    // for loop until we find a chunk that is large enough
    for (Chunk_T c = g_free_head; c; c = chunk_get_next_free(c)) {
        if (chunk_get_units(c) >= units) {
            remove_chunk(c);
            /* Split if large enough */
            // header and footer are needed so +2 is added in back
            if (chunk_get_units(c) > units + 2) {
                // split the chunk into two chunks
                Chunk_T split = (Chunk_T)((char *)c + units * CHUNK_UNIT);
                // set the size of the new chunk to the remaining size
                // size of c - unit = size of split
                chunk_set_units(split, chunk_get_units(c) - units);
                // set the status of the new chunk (split) to free
                chunk_set_footer(split);
                insert_chunk(split);
                // set the size of the original chunk to the requested size
                chunk_set_units(c, units);
            }
            // change state to used state
            chunk_set_status(c, CHUNK_IN_USE);
            chunk_set_footer(c);
            assert(check_heap_validity());
            return (char *)c + sizeof(struct Chunk);
        }
    }

    /* No fit found: extend heap */
    // define requested size 
    size_t req = units * CHUNK_UNIT;
    // add the heap size to the requested size
    // get the new size of heap
    // nc: new chunk which is used as new chunk after sbrk
    Chunk_T nc = (Chunk_T)sbrk(req);
    // If sbrk fails it returns -1 so check if sbrk fails
    if (nc == (Chunk_T)-1){
        return NULL;
    }
    // set the end of the heap to the new chunk
    g_heap_end = sbrk(0);

    // calculate the size of the new chunk
    chunk_set_units(nc, units);
    // set status of new chunk to free
    chunk_set_status(nc, CHUNK_FREE);
    // set the footer of the new chunk
    chunk_set_footer(nc);
    // insert_chunk(nc);
    insert_chunk(merge_chunks(nc));

    /* Retry allocation */
    return heapmgr_malloc(size);
}

/*--------------------------------------------------------------------*/
/* heapmgr_free:                                                      */
/*   Free a previously allocated block 'm'.  Marks the chunk free,   */
/*   writes footer, coalesces neighbors, and reinserts into free list*/
/*--------------------------------------------------------------------*/
void
heapmgr_free(void *m)
{
    // check if the pointer is NULL
    if (!m){
        return;
    }
    assert(check_heap_validity());

    // get the chunk header from the user pointer
    Chunk_T c = get_chunk_from_data_ptr(m);
    assert(chunk_get_status(c) == CHUNK_IN_USE);

    // set the status of the chunk to free
    chunk_set_status(c, CHUNK_FREE);
    // set the footer of the chunk
    chunk_set_footer(c);
    // merge the chunk with its neighbors if possible
    insert_chunk(merge_chunks(c));

    assert(check_heap_validity());
}
