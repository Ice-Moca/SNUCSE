/*---------------------------------------------------------------------------*/
/* dynarray.h                                                                */
/* Original author: Bob Dondero                                              */
/* Modified by: Jongki Park, Kyoungsoo Park                                  */
/*---------------------------------------------------------------------------*/

#include "dynarray.h"

enum {MIN_PHYS_LENGTH = 2};
enum {GROWTH_FACTOR = 2};

/*---------------------------------------------------------------------------*/
#ifndef NDEBUG
static int dynarray_is_valid(DynArray_T oDynArray) {
    if (oDynArray->iLength < 0) return 0;
    if (oDynArray->iPhysLength < MIN_PHYS_LENGTH) return 0;
    if (oDynArray->iLength > oDynArray->iPhysLength) return 0;
    if (oDynArray->ppvArray == NULL) return 0;
    return 1;
}
#endif
/*---------------------------------------------------------------------------*/
DynArray_T dynarray_new(int iLength) {
    DynArray_T oDynArray;

    assert(iLength >= 0);

    oDynArray = (struct DynArray*)malloc(sizeof(struct DynArray));
    assert(oDynArray != NULL);
    oDynArray->iLength = iLength;

    if (iLength > MIN_PHYS_LENGTH)
        oDynArray->iPhysLength = iLength;
    else
        oDynArray->iPhysLength = MIN_PHYS_LENGTH;
    
    oDynArray->ppvArray = (const void**)calloc((size_t)oDynArray->iPhysLength,
                                sizeof(void*));
    assert(oDynArray->ppvArray != NULL);

    return oDynArray;
}
/*---------------------------------------------------------------------------*/
void dynarray_free(DynArray_T oDynArray) {
    if (oDynArray == NULL)
        return;

    free(oDynArray->ppvArray);
    free(oDynArray);
}
/*---------------------------------------------------------------------------*/
int dynarray_get_length(DynArray_T oDynArray) {
  assert(oDynArray != NULL);
  assert(dynarray_is_valid(oDynArray));

  return oDynArray->iLength;
}
/*---------------------------------------------------------------------------*/
void *dynarray_get(DynArray_T oDynArray, int iIndex) {
    assert(oDynArray != NULL);
    assert(dynarray_is_valid(oDynArray));
    assert(iIndex >= 0);
    assert(iIndex < oDynArray->iLength);

    return (void*)(oDynArray->ppvArray)[iIndex];
}
/*---------------------------------------------------------------------------*/
void *dynarray_set(DynArray_T oDynArray, int iIndex, const void *element) {
    const void *pvOldElement;

    assert(oDynArray != NULL);
    assert(dynarray_is_valid(oDynArray));
    assert(iIndex >= 0);
    assert(iIndex < oDynArray->iLength);

    pvOldElement = oDynArray->ppvArray[iIndex];
    oDynArray->ppvArray[iIndex] = element;
    
    return (void*)pvOldElement;
}
/*---------------------------------------------------------------------------*/
/* Double the physical length of oDynArray. */
static void dynarray_grow(DynArray_T oDynArray) {
    assert(oDynArray != NULL);
    assert(dynarray_is_valid(oDynArray));

    oDynArray->iPhysLength *= GROWTH_FACTOR;
    oDynArray->ppvArray = (const void**)realloc(oDynArray->ppvArray,
                                sizeof(void*) * oDynArray->iPhysLength);
    
    assert(oDynArray->ppvArray != NULL);
}
/*---------------------------------------------------------------------------*/
int dynarray_add(DynArray_T oDynArray, const void *element) {
    assert(oDynArray != NULL);
    assert(dynarray_is_valid(oDynArray));

    if (oDynArray->iLength == oDynArray->iPhysLength)
        dynarray_grow(oDynArray);

    oDynArray->ppvArray[oDynArray->iLength] = element;
    oDynArray->iLength++;
    
    return 1;
}
/*---------------------------------------------------------------------------*/
void dynarray_map(DynArray_T oDynArray,
                void (*pfApply)(void *element, void *pvExtra),
                const void *pvExtra) {
  int i;

  assert(oDynArray != NULL);
  assert(dynarray_is_valid(oDynArray));
  assert(pfApply != NULL);

  for (i = 0; i < oDynArray->iLength; i++)
    (*pfApply)((void*)oDynArray->ppvArray[i], (void*)pvExtra);
}
/*---------------------------------------------------------------------------*/