#ifdef COMPILETIME
// Compile-time interposition of malloc and free using C
// preprocessor. A local malloc.h file defines malloc (free)
// as wrappers mymalloc (myfree) respectively.

#include <malloc.h>
#include <stdio.h>

//
// mymalloc - malloc wrapper function
//
void *mymalloc(size_t size, char *file, int line) {
  void *ptr = malloc(size);
  printf("%s:%d: malloc(%d)=%p\n", file, line, (int)size, ptr);
  return ptr;
}

void myfree(void *ptr, char *file, int line) {
  free(ptr);
  printf("%s:%d: free(%p)\n", file, line, ptr);
}

#endif

#ifdef LINKTIME
// Link-time interposition of malloc and free using
// the static linker's (ld)
// "--wrap symbol" flag.

#include <stdio.h>

void *__real_malloc(size_t size);
void __real_free(void *ptr);

//
// __wrap_malloc - malloc wrapper function
//
void *__wrap_malloc(size_t size) {
  void *ptr = __real_malloc(size);
  printf("malloc(%d) = %p\n", (int)size, ptr);
  return ptr;
}

//
// __wrap_free - free wrapper function
//
void __wrap_free(void *ptr) {
  __real_free(ptr);
  printf("free(%p)\n", ptr);
}

#endif

#ifdef RUNTIME
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void *malloc(size_t size) {
  static void *(*mallocp)(size_t size) = NULL;
  char *error;
  void *ptr;

  // get address of original libc malloc
  if (!mallocp) {
    void *sym;
    sym = dlsym(RTLD_NEXT, "malloc");
    *(void**)(&mallocp) = sym;
    if ((error = dlerror()) != NULL) {
      fputs(error, stderr);
      exit(EXIT_FAILURE);
    }
  }

  ptr = mallocp(size);

  /*
    Using standard I/O in the intercepted malloc function will cause a stack
    overflow, because in libc I/O, output to stdout is buffered. Note that this
    buffering might internally call malloc. In this case, if we use standard IO
    in malloc function, we will infinitely call malloc recursively. To avoid
    this, we write directly to the stdout file descriptor.
  */

  // char buf[100];
  // int len = sprintf(buf, "malloc(%d) = %p\n", (int)size, ptr);
  // write(STDOUT_FILENO, buf, len);

  // If you want to test above statement, comment out the following line
  printf("malloc(%d) = %p\n", (int)size, ptr);

  return ptr;
}

void free(void *ptr) {
  static void (*freep)(void *) = NULL;
  char *error;

  // get address of original libc free
  if (!freep) {
    void *sym;
    sym = dlsym(RTLD_NEXT, "free");
    *(void**)(&freep) = sym;
    if ((error = dlerror()) != NULL) {
      fputs(error, stderr);
      exit(EXIT_FAILURE);
    }
  }

  freep(ptr);
  printf("free(%p)\n", ptr);

  // char buf[100];
  // int len = sprintf(buf, "free(%p)\n", ptr);
  // write(STDOUT_FILENO, buf, len);
}

#endif
