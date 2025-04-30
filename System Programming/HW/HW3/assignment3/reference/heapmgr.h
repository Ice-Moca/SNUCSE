/*--------------------------------------------------------------------*/
/* heapmgr.h                                                          */
/* Author: KyoungSoo Park                                             */
/*--------------------------------------------------------------------*/

#ifndef HEAPMGR_INCLUDED
#define HEAPMGR_INCLUDED

#include <stddef.h>

void *heapmgr_malloc(size_t ui_bytes);
/* Return a pointer to space for an object of size ui_bytes. Return
   NULL if ui_bytes is 0 or the request cannot be satisfied. The
   space is uninitialized. */

void heapmgr_free(void *pv_bytes);
/* Deallocate the space pointed to by pv_bytes.  Do nothing if pv_bytes
   is NULL.  It is an unchecked runtime error for pv_bytes to be a
   pointer to space that was not previously allocated by
   heapmgr_malloc(). */

#endif