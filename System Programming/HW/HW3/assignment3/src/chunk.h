/* chunk.h */
/*--------------------------------------------------------------------*/
/* chunk.h                                                            */
/* Author: 2023-12753 EunSu Yeo                                       */
/*--------------------------------------------------------------------*/

#ifndef CHUNK_INCLUDED
#define CHUNK_INCLUDED

// used for size_t
#include <stddef.h>    

enum { CHUNK_UNIT = 8 };

/*
Each chunk has a size_status & 1 pointer.
- header: free_ptr is used as the next-free pointer.
- footer: free_ptr is used as the prev-free pointer.
*/
typedef struct Chunk {
    size_t       size_status;  // upper bits: size in units, LSB: status (got idea form 2024 Midterm) 
    struct Chunk *free_ptr;    // used for both header and footer
} *Chunk_T;

enum {
    // define chunk status as 0 or 1 
    // Because we will use status in bit operations.
    CHUNK_IN_USE = 0,
    CHUNK_FREE   = 1
};

/* Chunk size and status operations */
size_t chunk_get_units(Chunk_T c);
int    chunk_get_status(Chunk_T c);
void   chunk_set_units(Chunk_T c, size_t units);
void   chunk_set_status(Chunk_T c, int status);

/* Free list pointer operations */
Chunk_T chunk_get_next_free(Chunk_T c);
void    chunk_set_next_free(Chunk_T c, Chunk_T next);
Chunk_T chunk_get_prev_free(Chunk_T c);
void    chunk_set_prev_free(Chunk_T c, Chunk_T prev);

/* Adjacent chunk computation */
Chunk_T chunk_get_next_adjacent(Chunk_T c, void *heap_start, void *heap_end);

/* Chunk validity check */
int chunk_is_valid(Chunk_T c, void *heap_start, void *heap_end);

/* Footer management */
void   chunk_set_footer(Chunk_T c);
size_t chunk_get_footer_units(Chunk_T c);

#endif /* CHUNK_INCLUDED */
