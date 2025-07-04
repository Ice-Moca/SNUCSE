#include <stdio.h>
#include <stdlib.h>

#ifndef MYMALLOC_H
#define MYMALLOC_H

#define malloc(size) mymalloc(size, __FILE__, __LINE__)
#define free(ptr) myfree(ptr, __FILE__, __LINE__)

void *mymalloc(size_t size, char *file, int line);
void myfree(void *ptr, char *file, int line);

#endif