#include "vector.h"
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
  int N = argc > 2 ? atoi(argv[1]) : 0;
  if (N <= 0)
    N = 16;

  int *a = malloc(N * sizeof(int));
  int *b = malloc(N * sizeof(int));
  int *c = malloc(N * sizeof(int));
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
