/*--------------------------------------------------------------------*/
/* chunkbase.h                                                        */
/* Author: Donghwi Kim, KyoungSoo Park                                */
/*--------------------------------------------------------------------*/

#ifndef _CHUNK_BASE_H_
#define _CHUNK_BASE_H_

#pragma once

#include <stdbool.h>
#include <unistd.h>


/* 
   each chunk has a header and data units. each header in a chunk has
   a pointer to the next chunk in the free list. the size of a chunk
   is in the number of units, but it does not include the unit for a
   header. For example, if a chunk has 5 units, its actual size is 6
   units since it has one header.
*/

typedef struct Chunk *Chunk_T;

enum {
   CHUNK_FREE,
   CHUNK_IN_USE,
};

enum {
   CHUNK_UNIT = 16,        /* 16 = sizeof(struct Chunk) */
};

/* chunk_get_status:
 * Returns a chunk's status which shows whether the chunk is in use or free.
 * Return value is either CHUNK_IN_USE or CHUNK_FREE. */
int
chunk_get_status(Chunk_T c);

/* chunk_set_status:
 * Set the status of the chunk, 'c'. 
 * status can be either CHUNK_FREE or CHUNK_IN_USE */
void
chunk_set_status(Chunk_T c, int status);

/* chunk_get_units:
 * Returns the size of a chunk, 'c', in terms of the number of chunk units. */
int
chunk_get_units(Chunk_T c);

/* chunk_set_units:
 * Sets the current size in 'units' of 'c' */
void
chunk_set_units(Chunk_T c, int units);

/* chunk_get_next_free_chunk:
 * Returns the next free chunk in free chunk list.
 * Returns NULL if 'c' is the last free chunk in the list. */
Chunk_T
chunk_get_next_free_chunk(Chunk_T c);

/* chunk_set_next_free_chunk:
 * Sets the next free chunk of 'c' to 'next') */
void
chunk_set_next_free_chunk(Chunk_T c, Chunk_T next);

/* chunk_get_next_adjacent:
 * Returns the next adjacent chunk to 'c' in memory space.
 * start is the pointer to the start of the Heap
 * end is the the pointer to the end of the Heap
 * Returns NULL if 'c' is the last chunk in memory space. */
Chunk_T
chunk_get_next_adjacent(Chunk_T c, void *start, void *end);

/* Following two functions are for debugging.
 * These will be removed by C preprocessor if you compile the code with
 * -DNDEBUG option. 
 */
#ifndef NDEBUG
/* chunk_is_valid:
 * Checks the validity of a chunk, 'c'. Returns 1 if OK otherwise 0.
 * start is the pointer to the start of the Heap
 * end is the the pointer to the end of the Heap
 */
int 
chunk_is_valid(Chunk_T c, void *start, void *end);

#endif /* NDEBUG */

#endif /* _CHUNK_BASE_H_ */