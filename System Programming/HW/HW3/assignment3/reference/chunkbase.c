/*--------------------------------------------------------------------*/
/* chunkbase.c                                                        */
/* Author: Donghwi Kim, KyoungSoo Park                                */
/*--------------------------------------------------------------------*/

#include <stdio.h>
#include <stddef.h>
#include <unistd.h>
#include <stdlib.h>
#include <assert.h>

#include "chunkbase.h"

struct Chunk {
   Chunk_T next;       /* Pointer to the next chunk in the free chunk list */
   int units;          /* Capacity of a chunk (chunk units) */
   int status;         /* CHUNK_FREE or CHUNK_IN_USE */
};

/*--------------------------------------------------------------------*/
int
chunk_get_status(Chunk_T c)
{
   return c->status;
}
/*--------------------------------------------------------------------*/
void
chunk_set_status(Chunk_T c, int status)
{
   c->status = status;
}
/*--------------------------------------------------------------------*/
int
chunk_get_units(Chunk_T c)
{
   return c->units;
}
/*--------------------------------------------------------------------*/
void
chunk_set_units(Chunk_T c, int units)
{
   c->units = units;
}
/*--------------------------------------------------------------------*/
Chunk_T
chunk_get_next_free_chunk(Chunk_T c)
{
  return c->next;
}
/*--------------------------------------------------------------------*/
void
chunk_set_next_free_chunk(Chunk_T c, Chunk_T next)
{
   c->next = next;
}
/*--------------------------------------------------------------------*/
Chunk_T
chunk_get_next_adjacent(Chunk_T c, void* start, void* end)
{
   Chunk_T n;

   assert((void *)c >= start);

   /* Note that a chunk consists of one chunk unit for a header, and
    * many chunk units for data. */
   n = c + c->units + 1;

   /* If 'c' is the last chunk in memory space, then return NULL. */
   if ((void *)n >= end)
      return NULL;
   
   return n;
}

#ifndef NDEBUG
/*--------------------------------------------------------------------*/
int 
chunk_is_valid(Chunk_T c, void *start, void *end)
/* Return 1 (TRUE) iff c is valid */
{
   assert(c != NULL);
   assert(start != NULL);
   assert(end != NULL);

   if (c < (Chunk_T)start)
      {fprintf(stderr, "Bad heap start\n"); return 0; }
   if (c >= (Chunk_T)end)
      {fprintf(stderr, "Bad heap end\n"); return 0; }
   if (c->units == 0)
      {fprintf(stderr, "Zero units\n"); return 0; }
   return 1;
}
#endif