#include "vector.h"
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

void initvec(int *v, int N) {
  for (int i = 0; i < N; i++)
    v[i] = rand() % 10;
}
void printvec(char *label, int *v, int N) {
  printf("%8s: ", label);
  for (int i = 0; i < N; i++)
    printf("%4d%s", v[i], i < N - 1 ? " " : "\n");
}

int main(int argc, char *argv[]) {
  //
  // load shared library
  //
  void *handle;
  handle = dlopen("./libvector.so", RTLD_LAZY);
  if (!handle) {
    perror("Cannot load library");
    return EXIT_FAILURE;
  }

  //
  // obtain addresses of library functions
  //
  void (*addvec)(int *, int *, int *, int);
  void (*mulvec)(int *, int *, int *, int);
  void *sym;
  sym = dlsym(handle, "addvec");
  *(void **)(&addvec) = sym;
  sym = dlsym(handle, "mulvec");
  *(void **)(&mulvec) = sym;

  if (!addvec || !mulvec) {
    perror("Cannot find functions");
    return EXIT_FAILURE;
  }

  int N = argc == 2 ? atoi(argv[1]) : 10;

  int *a = malloc(N * sizeof(int));
  int *b = malloc(N * sizeof(int));
  int *c = malloc(N * sizeof(int));

  // check malloc
  if (!a || !b || !c) {
    perror("Cannot allocate memory");
    return EXIT_FAILURE;
  }

  initvec(a, N);
  initvec(b, N);

  printvec("a", a, N);
  printvec("b", b, N);

  addvec(c, a, b, N);
  printvec("a+b", c, N);

  mulvec(c, a, b, N);
  printvec("a*b", c, N);

  free(a);
  free(b);
  free(c);

  return EXIT_SUCCESS;
}
