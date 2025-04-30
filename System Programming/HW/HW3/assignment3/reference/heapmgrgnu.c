/*--------------------------------------------------------------------*/
/* heapmgrgnu.c                                                       */
/* Author: Bob Dondero                                                */
/* Using the GNU malloc() and free()                                  */
/*--------------------------------------------------------------------*/

#include "heapmgr.h"
#include <stdlib.h>

/*--------------------------------------------------------------------*/

void *heapmgr_malloc(size_t ui_bytes)

/* Return a pointer to space for an object of size ui_bytes. Return
   NULL if ui_bytes is 0 or the request cannot be satisfied. The
   space is uninitialized. */

{
   return malloc(ui_bytes);
}

/*--------------------------------------------------------------------*/

void heapmgr_free(void *pv_bytes)

/* Deallocate the space pointed to by pv_bytes. Do nothing if pvBytes
   is NULL. It is an unchecked runtime error for pv_bytes to be a
   a pointer to space that was not previously allocated by
   heapmgr_malloc(). */

{
   free(pv_bytes);
}