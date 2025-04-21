#include <stdio.h>
#include <stdlib.h>

// Slide 05

void swap();

int buf[2] = {1, 2};

int main() {
  printf("[ %d, %d ]\n", buf[0], buf[1]);
  swap();
  printf("[ %d, %d ]\n", buf[0], buf[1]);
  return EXIT_SUCCESS;
}
