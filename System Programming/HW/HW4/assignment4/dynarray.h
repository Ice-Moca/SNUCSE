/*---------------------------------------------------------------------------*/
/* dynarray.h                                                                */
/* Original author: Bob Dondero                                              */
/* Modified by: Jongki Park, Kyoungsoo Park                                  */
/*---------------------------------------------------------------------------*/

#ifndef _DYNARRAY_H_
#define _DYNARRAY_H_

#include <stdlib.h>
#include <assert.h>

/* A DynArray consists of an array, along with its logical and
   physical lengths. 
   
   In user interaction-heavy programs like Shell, 
   responsiveness is important, so it's inefficient to individually allocate 
   tokens with malloc for each user input command.
   
   To improve this, we allocate and use blocks of memory in advance, 
   where iLength represents the logical length of the array 
   as seen by the user, and iPhysLength represents the physical length 
   of the actual allocated array. 
   
   This allows us to improve performance 
   by reducing the frequency of dynamic memory allocations. */
struct DynArray {
  /* The number of elements in the DynArray from the user's
     point of view. */
    int iLength;

  /* The number of elements in the array that underlies the
     DynArray. */
    int iPhysLength;

  /* The array that underlies the DynArray. */
    const void **ppvArray;
};


/* A DynArray_T is an array whose length can expand dynamically. */
typedef struct DynArray *DynArray_T;


/* Return a new oDynArray_T whose length is iLength.
   It is a checked runtime error for iLength to be negative. */
DynArray_T dynarray_new(int iLength);


/* Free oDynArray. Note that the prefix o indicates that it is an object */
void dynarray_free(DynArray_T oDynArray);


/* Return the length of DynArray.
   It is a checked runtime error for oDynArray to be NULL. */
int dynarray_get_length(DynArray_T oDynArray);


/* Return the i'th Index element of oDynArray.
   It is a checked runtime error for oDynArray to be NULL.
   It is a checked runtime error for i'th Index to be less than 0 or
   greater than or equal to the length of oDynArray. */
void *dynarray_get(DynArray_T oDynArray, int iIndex);


/* Assign element to the i'th Index element of oDynArray.  
   Returns the old element.
   It is a checked runtime error for oDynArray to be NULL.
   It is a checked runtime error for iIndex to be less than 0 or
   greater than or equal to the length of oDynArray. */
void *dynarray_set(DynArray_T oDynArray, int iIndex,
    const void *element);


/* Add element to the end of oDynArray, thus incrementing its length.
   It is a checked runtime error for oDynArray to be NULL. */
int dynarray_add(DynArray_T oDynArray, const void *element);


/* Apply function *pfApply to each element of oDynArray, passing
   pvExtra as an extra argument.  That is, for each element element of
   oDynArray, call (*pfApply)(element, pvExtra).
   It is a checked runtime error for oDynArray or pfApply to be
   NULL. */
void dynarray_map(DynArray_T oDynArray,
    void (*pfApply)(void *element, void *pvExtra),
    const void *pvExtra);


#endif /* _DYNARRAY_H_ */