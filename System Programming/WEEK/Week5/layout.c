#define _GNU_SOURCE
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define N 1024 * 1024

// Slide 25

int global_int = 0;
int global_arr[N];
int *global_ptr;
int *shared_int; // Pointer for shared memory

struct __shared {
  sem_t m;
  int shared_int;
} * shared;

void foo(void) {
  // No implementation
}

void bar(unsigned int key, int val) {
  // No implementation
}

int main(int argc, char *argv[]) {
  int local_arr[1024];
  int local_k = 0, local_v = 0;

  // Determine number of processes (default: 1)
  int nproc = 0;
  if (argc > 1) {
    nproc = atoi(argv[1]); // Convert input to integer
    if (nproc <= 0) {
      fprintf(stderr, "Invalid number of processes. Using default: 1\n");
      nproc = 1;
    }
  }

  // Allocate memory for shared_int using mmap()
  shared = (struct __shared *)mmap(NULL, sizeof(struct __shared),
                                   PROT_READ | PROT_WRITE,
                                   MAP_SHARED | MAP_ANONYMOUS, 0, 0);
  if (shared == MAP_FAILED) {
    perror("Cannot map shared memory");
    exit(EXIT_FAILURE);
  }

  sem_init(&shared->m, 1, 1);
  shared->shared_int = 0;

  // Fork multiple processes
  while (nproc > 1) {
    if (fork() == 0)
      break;
    nproc--;
  }

  // Allocate memory for global_ptr using malloc
  global_ptr = malloc(sizeof(int));
  // Even malloc can fail: check for errors
  if (global_ptr == NULL) {
    perror("Cannot allocate memory");
    exit(EXIT_FAILURE);
  }

  int delay = nproc;
  int pid = getpid();
  printf("[%d] Memory addresses\n"
         "  &foo():        %p\n"
         "  &bar():        %p\n"
         "  &main():       %p\n"
         "\n"
         "  &global_int:   %p\n"
         "  &global_arr:   %p\n"
         "  &global_ptr:   %p\n"
         "\n"
         "  &local_arr:    %p\n"
         "  &local_k:      %p\n"
         "  &local_v:      %p\n"
         "\n"
         "   global_ptr:   %p\n"
         "   shared_int:   %p\n"
         "\n\n",
         pid, (void *)(intptr_t)&foo, (void *)(intptr_t)&bar,
         (void *)(intptr_t)&main, (void *)&global_int, (void *)&global_arr,
         (void *)&global_ptr, (void *)&local_arr, (void *)&local_k,
         (void *)&local_v, (void *)global_ptr, (void *)&shared->shared_int);

  while (1) {
    //
    // endless loop increasing global_int / shared_int
    //

    printf("[%d] global_int = mem[%p] = %d; shared_int = mem[%p] = %d\n",
           getpid(), (void *)&global_int, global_int,
           (void *)&shared->shared_int, shared->shared_int);

    global_int++;
    sem_wait(&shared->m);
    shared->shared_int++;
    sem_post(&shared->m);

    sleep(delay);
  }

  // Free allocated memory
  free(global_ptr);
  sem_destroy(&shared->m);
  munmap(shared, sizeof(struct __shared));

  return EXIT_SUCCESS;
}
