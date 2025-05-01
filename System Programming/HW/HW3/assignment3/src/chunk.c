/*--------------------------------------------------------------------*/
/* chunk.c                                                            */
/* Author: 2023-12753 EunSu Yeo                                       */
/*--------------------------------------------------------------------*/

#include "chunk.h"
#include <assert.h>

/* Part1: Chunk size and status operations */

// return the size of the chunk in units
// size_status is stored in upper bits so Left shift to get the size
size_t chunk_get_units(Chunk_T c) {
    assert(c);
    // Left shift by 1
    return c->size_status >> 1;
}

// return the status of the chunk
// status is stored in LSB so AND operation with 1 to get the status
int chunk_get_status(Chunk_T c) {
    assert(c);
    // &1
    return c->size_status & 1;
}

// set the size_status of the chunk
void chunk_set_units(Chunk_T c, size_t units) {
    assert(c);
    // get the status of the chunk
    int st = chunk_get_status(c);
    // with the given units, which is size
    // Left shift the size by 1 and then use the OR operation to set the status
    c->size_status = (units << 1) | st;
}

// set the status of the chunk
void chunk_set_status(Chunk_T c, int status) {
    assert(c);
    // get the size of the chunk
    size_t u = chunk_get_units(c);
    // use AND operation to always get the value 0 or 1
    c->size_status = (u << 1) | (status & 1);
}

/* Part2: Free list pointer operations */

/* next_free: header->free_ptr */
Chunk_T chunk_get_next_free(Chunk_T c) {
    assert(c);
    // give the pointer of header
    // which means the next free chunk
    return c->free_ptr;
}

void chunk_set_next_free(Chunk_T c, Chunk_T next) {
    assert(c);
    // set the next free chunk pointer to given next pointer
    // which will be only used in header
    c->free_ptr = next;
}

/* prev_free: footer->free_ptr */
Chunk_T chunk_get_prev_free(Chunk_T c) {
    assert(c);
    // get the size of the chunk
    size_t units = chunk_get_units(c);
    // calculate the address of footer 
    // which is in the last part fo the chunk
    // footer = header + size - sizeof(footer)
    Chunk_T footer = (Chunk_T)((char *)c + units * CHUNK_UNIT - sizeof(*footer));
    return footer->free_ptr;
}

void chunk_set_prev_free(Chunk_T c, Chunk_T prev) {
    assert(c);
    // get the size of the chunk
    size_t units = chunk_get_units(c);
    // calculate the address of footer 
    Chunk_T footer = (Chunk_T)((char *)c + units * CHUNK_UNIT - sizeof(*footer));
    // set the prev free chunk pointer to given prev pointer
    // which will be only used in footer
    footer->free_ptr = prev;
}

/* Part3: Adjacent chunk computation */

Chunk_T chunk_get_next_adjacent(Chunk_T c, void *heap_start, void *heap_end) {
    assert(c);
    // calculate the address of next chunk
    Chunk_T next = (Chunk_T)((char *)c + (chunk_get_units(c) * CHUNK_UNIT));
    // if the next chunk is out of the range of heap return NULL
    if((void *)next>= heap_end){
        return NULL;
    }
    // else return the next chunk
    return next;
}

Chunk_T chunk_get_prev_adjacent(Chunk_T c, void *heap_start, void *heap_end) {
    assert(c);
    if ((void*)c <= heap_start) {
        return NULL;
    }
    // calculate the address of footer
    Chunk_T footer = (Chunk_T)((char*)c - sizeof(*c));
    // get the size of the chunk from footer by Left shift by 1
    size_t prev_units = footer->size_status >> 1;
    // calculate the address of previous chunk
    Chunk_T prev = (Chunk_T)((char*)c - prev_units * CHUNK_UNIT);
    if ((void*)prev < heap_start || (void*)prev >= heap_end) {
        return NULL;
    }
    return prev;
}

/* Part4: Chunk validity check */

int chunk_is_valid(Chunk_T c, void *heap_start, void *heap_end) {
    // check if the chunk is NULL or Not in the range of heap
    if (!c || (void *)c < heap_start || (void *)c >= heap_end){
        return 0;
    }
    // check if the chunk has not 0 units
    if (chunk_get_units(c) == 0){
        return 0;
    } 
    return 1;
}

/* Part5: Footer management */

/* Write header's size_status into footer */
void chunk_set_footer(Chunk_T c) {
    assert(c);
    // get the size of the chunk
    size_t units = chunk_get_units(c);
    Chunk_T footer = (Chunk_T)((char *)c + units * CHUNK_UNIT - sizeof(*footer));
    // set the footer's size_status to the header's size_status
    // same to the header's size_status
    footer->size_status = c->size_status;
}

/* Read units from footer */
size_t chunk_get_footer_units(Chunk_T c) {
    assert(c);
    // get the size of the chunk
    size_t units = chunk_get_units(c);
    // calculate the address of footer
    Chunk_T footer = (Chunk_T)((char *)c + units * CHUNK_UNIT - sizeof(*footer));
    // get the size of the chunk from footer by Left shift by 1
    return (footer->size_status >> 1);
}
