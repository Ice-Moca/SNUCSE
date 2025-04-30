/*--------------------------------------------------------------------*/
/* testheapmgr.c                                                      */
/* Author: Bob Dondero                                                */
/* modifyed by Juyoung Park                                           */
/*--------------------------------------------------------------------*/

#include "heapmgr.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <assert.h>
#include <sys/time.h>
#include <sys/resource.h>

#ifndef __USE_MISC
#define __USE_MISC
#endif
#include <unistd.h>

enum {FALSE, TRUE};

/*--------------------------------------------------------------------*/

/* These arrays are too big for the stack section, so store
   them in the bss section. */

/* The maximum allowable number of calls of heapmgr_malloc(). */
enum {MAX_CALLS = 1000000};

/* Memory chunks allocated by heapmgr_malloc(). */
static char *apc_chunks[MAX_CALLS];

/* Randomly generated chunk sizes.  */
static int ai_sizes[MAX_CALLS];

/*--------------------------------------------------------------------*/

/* Function declarations. */

static void get_args(int argc, char *argv[],
   int *pi_test_num, int *pi_count, int *pi_size);
static void set_cpu_limit(void);
static void test_LIFO_fixed_malloc(int i_count, int i_size);
static void test_LIFO_fixed_free(int i_count, int i_size);
static void test_FIFO_fixed_malloc(int i_count, int i_size);
static void test_FIFO_fixed_free(int i_count, int i_size);
static void test_LIFO_random_malloc(int i_count, int i_size);
static void test_LIFO_random_free(int i_count, int i_size);
static void test_FIFO_random_malloc(int i_count, int i_size);
static void test_FIFO_random_free(int i_count, int i_size);
static void test_random_fixed(int i_count, int i_size);
static void test_random_random(int i_count, int i_size);
static void test_worst(int i_count, int i_size);

/*--------------------------------------------------------------------*/

/* apc_test_name is an array containing the names of the tests. */

static char *apc_test_name[] =
{
   "LIFO_fixed", "FIFO_fixed", "LIFO_random", "FIFO_random",
   "random_fixed", "random_random", "worst"
};

/*--------------------------------------------------------------------*/

/* apf_test_function is an array containing pointers to the test
   functions.  Each pointer corresponds, by position, to a test name
   in apc_test_name. */

typedef void (*test_function)(int, int);
static test_function apf_test_function[] =
{
   test_LIFO_fixed_malloc, test_FIFO_fixed_malloc, test_LIFO_random_malloc, test_FIFO_random_malloc,
   test_random_fixed, test_random_random, test_worst,
   test_LIFO_fixed_free, test_FIFO_fixed_free, test_LIFO_random_free, test_FIFO_random_free
};

/*--------------------------------------------------------------------*/

int main(int argc, char *argv[])

/* Test the heapmgr_malloc() and heapmgr_free() functions.

   argv[1] indicates which test to run:
      LIFO_fixed: LIFO with fixed size chunks,
      FIFO_fixed: FIFO with fixed size chunks,
      LIFO_random: LIFO with random size chunks,
      FIFO_random: FIFO with random size chunks,
      random_fixed: random order with fixed size chunks,
      random_random: random order with random size chunks,
      worst: worst case for single linked list implementation.

   argv[2] is the number of calls of heapmgr_malloc() and heapmgr_free()
   to execute.  argv[2] cannot be greater than MAX_CALLS.

   argv[3] is the (maximum) size of each memory chunk.

   If the NDEBUG macro is not defined, then initialize and check
   the contents of each memory chunk.

   At the end of the process, write the heap memory and CPU time
   consumed to stdout, and return 0. */

{
   int i_test_num = 0;
   int i_count = 0;
   int i_size = 0;
   clock_t i_initial_clock, i_malloc_clock, i_final_clock;
   char *pc_initial_break, *pc_final_break;
   long long i_memory_consumed;
   double d_malloc_time, d_free_time, d_total_time;

   //srand((unsigned int)time(NULL));

   /* Get the command-line arguments. */
   get_args(argc, argv, &i_test_num, &i_count, &i_size);

   /* Start printing the results. */
   printf("%17s %13s %7d %6d ", argv[0], argv[1], i_count, i_size);
   fflush(stdout);

   /* Save the initial clock and program break. */
   i_initial_clock = clock();
   pc_initial_break = sbrk(0);

   /* Set the process's CPU time limit. */
   set_cpu_limit();

   if (i_test_num < 4) {
      (*(apf_test_function[i_test_num]))(i_count, i_size);
      i_malloc_clock = clock();
      (*(apf_test_function[i_test_num + 7]))(i_count, i_size);
      i_final_clock = clock();
      pc_final_break = sbrk(0);

      d_malloc_time = ((double)(i_malloc_clock - i_initial_clock)) / CLOCKS_PER_SEC;
      d_free_time = ((double)(i_final_clock - i_malloc_clock)) / CLOCKS_PER_SEC;
      d_total_time = ((double)(i_final_clock - i_initial_clock)) / CLOCKS_PER_SEC;

      i_memory_consumed = (long long)(pc_final_break - pc_initial_break);

      printf("%6.2f %6.2f %6.2f %10lld\n", d_malloc_time, d_free_time, d_total_time, i_memory_consumed);
   }
   else {
      (*(apf_test_function[i_test_num]))(i_count, i_size);

      i_final_clock = clock();
      pc_final_break = sbrk(0);

      d_total_time = ((double)(i_final_clock - i_initial_clock)) / CLOCKS_PER_SEC;
      i_memory_consumed = (long long)(pc_final_break - pc_initial_break);

      printf("     -      - %6.2f %10lld\n", d_total_time, i_memory_consumed);
   }

   return 0;
}

/*--------------------------------------------------------------------*/

static void get_args(int argc, char *argv[],
   int *pi_test_num, int *pi_count, int *pi_size)

/* Get command-line arguments *pi_test_num, *pi_count, and *pi_size,
   from argument vector argv.  argc is the number of used elements
   in argv.  Exit if any of the arguments is invalid.  */

{
   int i;
   int i_test_count;

   if (argc != 4)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      exit(EXIT_FAILURE);
   }

   /* Get the test number. */
   i_test_count = (int)(sizeof(apc_test_name) / sizeof(apc_test_name[0]));
   for (i = 0; i < i_test_count; i++)
      if (strcmp(argv[1], apc_test_name[i]) == 0)
      {
         *pi_test_num = i;
         break;
      }
   if (i == i_test_count)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      fprintf(stderr, "Valid testnames:\n");
      for (i = 0; i < i_test_count; i++)
         fprintf(stderr, " %s", apc_test_name[i]);
      fprintf(stderr, "\n");
      exit(EXIT_FAILURE);
   }

   /* Get the count. */
   if (sscanf(argv[2], "%d", pi_count) != 1)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      fprintf(stderr, "Count must be numeric\n");
      exit(EXIT_FAILURE);
   }
   if (*pi_count <= 0)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      fprintf(stderr, "Count must be positive\n");
      exit(EXIT_FAILURE);
   }
   if (*pi_count > MAX_CALLS)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      fprintf(stderr, "Count cannot be greater than %d\n", MAX_CALLS);
      exit(EXIT_FAILURE);
   }

   /* Get the size. */
   if (sscanf(argv[3], "%d", pi_size) != 1)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      fprintf(stderr, "Size must be numeric\n");
      exit(EXIT_FAILURE);
   }
   if (*pi_size <= 0)
   {
      fprintf(stderr, "Usage: %s testname count size\n", argv[0]);
      fprintf(stderr, "Size must be positive\n");
      exit(EXIT_FAILURE);
   }
}

/*--------------------------------------------------------------------*/

static void set_cpu_limit(void)

/* Set the process's resource limit to 300 seconds (5 minutes).
   After 300 seconds, the OS will send a SIGKILL signal to the
   process. */

{
   struct rlimit s_rlimit;
   s_rlimit.rlim_cur = 300;
   s_rlimit.rlim_max = 300;
   setrlimit(RLIMIT_CPU, &s_rlimit);
}

/*--------------------------------------------------------------------*/

#define ASSURE(i) assure(i, __LINE__)

static void assure(int i_successful, int i_lineNum)

/* If !i_successful, print an error message indicating that the test
   at line i_lineNum failed. */

{
   if (! i_successful)
      fprintf(stderr, "Test at line %d failed.\n", i_lineNum);
}

/*--------------------------------------------------------------------*/

static void test_LIFO_fixed_malloc(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of size i_size, in
   last-in-first-out order. */

{
   int i;

   /* Call heapmgr_malloc() repeatedly to fill apc_chunks. */
   for (i = 0; i < i_count; i++)
   {
      apc_chunks[i] = (char*)heapmgr_malloc((size_t)i_size);
      ASSURE(apc_chunks[i] != NULL);

      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < i_size; i_col++)
            apc_chunks[i][i_col] = c;
      }
      #endif
   }
}

static void test_LIFO_fixed_free(int i_count, int i_size)

{
   int i;

   /* Call heapmgr_free() repeatedly to free the chunks in
      LIFO order. */
   for (i = i_count - 1; i >= 0; i--)
   {
      #ifndef NDEBUG
      {
         /* Check the chunk that is about to be freed to make sure
            that its contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < i_size; i_col++)
            ASSURE(apc_chunks[i][i_col] == c);
      }
      #endif

      heapmgr_free(apc_chunks[i]);
   }
}


/*--------------------------------------------------------------------*/

static void test_FIFO_fixed_malloc(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of size i_size, in
   first-in-first-out order. */

{
   int i;

   /* Call heapmgr_malloc() repeatedly to fill apc_chunks. */
   for (i = 0; i < i_count; i++)
   {
      apc_chunks[i] = (char*)heapmgr_malloc((size_t)i_size);
      ASSURE(apc_chunks[i] != NULL);

      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < i_size; i_col++)
            apc_chunks[i][i_col] = c;
      }
      #endif
   }
}

static void test_FIFO_fixed_free(int i_count, int i_size)

{
   int i;

   /* Call heapmgr_free() repeatedly to free the chunks in
      FIFO order. */
   for (i = 0; i < i_count; i++)
   {
      #ifndef NDEBUG
      {
         /* Check the chunk that is about to be freed to make sure
            that its contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < i_size; i_col++)
            ASSURE(apc_chunks[i][i_col] == c);
      }
      #endif

      heapmgr_free(apc_chunks[i]);
   }
}

/*--------------------------------------------------------------------*/

static void test_LIFO_random_malloc(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of some random size
   less than i_size, in last-in-first-out order. */

{
   int i;

   /* Fill ai_sizes, an array of random integers in the range 1 to
      i_size. */
   for (i = 0; i < i_count; i++)
      ai_sizes[i] = (rand() % i_size) + 1;

   /* Call heapmgr_malloc() repeatedly to fill apc_chunks. */
   for (i = 0; i < i_count; i++)
   {
      apc_chunks[i] = (char*)heapmgr_malloc((size_t)ai_sizes[i]);
      ASSURE(apc_chunks[i] != NULL);

      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < ai_sizes[i]; i_col++)
            apc_chunks[i][i_col] = c;
      }
      #endif
   }
}

static void test_LIFO_random_free(int i_count, int i_size)

{
   int i;

   /* Call heapmgr_free() repeatedly to free the chunks in
      LIFO order. */
   for (i = i_count - 1; i >= 0; i--)
   {
      #ifndef NDEBUG
      {
         /* Check the chunk that is about to be freed to make sure
            that its contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < ai_sizes[i]; i_col++)
            ASSURE(apc_chunks[i][i_col] == c);
      }
      #endif

      heapmgr_free(apc_chunks[i]);
   }
}

/*--------------------------------------------------------------------*/

static void test_FIFO_random_malloc(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of some random size
   less than i_size, in first-in-first-out order. */

{
   int i;

   /* Fill ai_sizes, an array of random integers in the range 1 to
      i_size. */
   for (i = 0; i < i_count; i++)
      ai_sizes[i] = (rand() % i_size) + 1;

   /* Call heapmgr_malloc() repeatedly to fill apc_chunks. */
   for (i = 0; i < i_count; i++)
   {
      apc_chunks[i] = (char*)heapmgr_malloc((size_t)ai_sizes[i]);
      ASSURE(apc_chunks[i] != NULL);

      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < ai_sizes[i]; i_col++)
            apc_chunks[i][i_col] = c;
      }
      #endif
   }
}

static void test_FIFO_random_free(int i_count, int i_size)

{
   int i;

   /* Call heapmgr_free() repeatedly to free the chunks in
      FIFO order. */
   for (i = 0; i < i_count; i++)
   {
      #ifndef NDEBUG
      {
         /* Check the chunk that is about to be freed to make sure
            that its contents haven't been corrupted. */
         int i_col;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < ai_sizes[i]; i_col++)
            ASSURE(apc_chunks[i][i_col] == c);
      }
      #endif

      heapmgr_free(apc_chunks[i]);
   }
}

/*--------------------------------------------------------------------*/

static void test_random_fixed(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of size i_size, in
   a random order. */

{
   int i;
   int i_rand;
   int i_logical_array_size;

   i_logical_array_size = (i_count / 3) + 1;

   /* Call heapmgr_malloc() and heapmgr_free() in a randomly
      interleaved manner. */
   i_rand = 0;
   for (i = 0; i < i_count; i++)
   {
      apc_chunks[i_rand] = (char*)heapmgr_malloc((size_t)i_size);
      ASSURE(apc_chunks[i_rand] != NULL);
      
      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         int i_col;
         char c = (char)((i_rand % 10) + '0');
         for (i_col = 0; i_col < i_size; i_col++)
            apc_chunks[i_rand][i_col] = c;
      }
      #endif

      /* Assign some random integer to i_rand. */
      i_rand = rand() % i_logical_array_size;

      /* If apc_chunks[i_rand] contains a chunk, free it and set
         apc_chunks[i_rand] to NULL. */
      if (apc_chunks[i_rand] != NULL)
      {
         #ifndef NDEBUG
         {
            /* Check the chunk that is about to be freed to make sure
               that its contents haven't been corrupted. */
            int i_col;
            char c = (char)((i_rand % 10) + '0');
            for (i_col = 0; i_col < i_size; i_col++)
               ASSURE(apc_chunks[i_rand][i_col] == c);
         }
         #endif

         heapmgr_free(apc_chunks[i_rand]);
         apc_chunks[i_rand] = NULL;
      }
   }

   /* Free the rest of the chunks. */
   for (i = 0; i < i_logical_array_size; i++)
   {
      if (apc_chunks[i] != NULL)
      {
         #ifndef NDEBUG
         {
            /* Check the chunk that is about to be freed to make sure
               that its contents haven't been corrupted. */
            int i_col;
            char c = (char)((i % 10) + '0');
            for (i_col = 0; i_col < i_size; i_col++)
               ASSURE(apc_chunks[i][i_col] == c);
         }
         #endif

         heapmgr_free(apc_chunks[i]);
         apc_chunks[i] = NULL;
      }
   }
}

/*--------------------------------------------------------------------*/

static void test_random_random(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of some random size
   less than i_size, in a random order. */

{
   int i;
   int i_rand;
   int i_logical_array_size;

   i_logical_array_size = (i_count / 3) + 1;

   /* Fill ai_sizes, an array of random integers in the range 1
      to i_size. */
   for (i = 0; i < i_logical_array_size; i++)
      ai_sizes[i] = (rand() % i_size) + 1;

   /* Call heapmgr_malloc() and heapmgr_free() in a randomly
      interleaved manner. */
   i_rand = 0;
   for (i = 0; i < i_count; i++)
   {
      apc_chunks[i_rand] = (char*)heapmgr_malloc((size_t)ai_sizes[i_rand]);
      ASSURE(apc_chunks[i_rand] != NULL);

      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         int i_col;
         char c = (char)((i_rand % 10) + '0');
         for (i_col = 0; i_col < ai_sizes[i_rand]; i_col++)
            apc_chunks[i_rand][i_col] = c;
      }
      #endif

      /* Assign some random integer to i_rand. */
      i_rand = rand() % i_logical_array_size;

      /* If apc_chunks[i_rand] contains a chunk, free it and set
         apc_chunks[i_rand] to NULL. */
      if (apc_chunks[i_rand] != NULL)
      {
         #ifndef NDEBUG
         {
            /* Check the chunk that is about to be freed to make sure
               that its contents haven't been corrupted. */
            int i_col;
            char c = (char)((i_rand % 10) + '0');
            for (i_col = 0; i_col < ai_sizes[i_rand]; i_col++)
               ASSURE(apc_chunks[i_rand][i_col] == c);
         }
         #endif

         heapmgr_free(apc_chunks[i_rand]);
         apc_chunks[i_rand] = NULL;
      }
   }

   /* Free the rest of the chunks. */
   for (i = 0; i < i_logical_array_size; i++)
   {
      if (apc_chunks[i] != NULL)
      {
         #ifndef NDEBUG
         {
            /* Check the chunk that is about to be freed to make sure
               that its contents haven't been corrupted. */
            int i_col;
            char c = (char)((i % 10) + '0');
            for (i_col = 0; i_col < ai_sizes[i]; i_col++)
               ASSURE(apc_chunks[i][i_col] == c);
         }
         #endif

         heapmgr_free(apc_chunks[i]);
         apc_chunks[i] = NULL;
      }
   }
}

/*--------------------------------------------------------------------*/

static void test_worst(int i_count, int i_size)

/* Allocate and free i_count memory chunks, each of some size less
   than i_size, in the worst possible order for a heapmgr that is
   implemented using a single linked list. */

{
   int i;

   /* Fill the array with chunks of increasing size, each separated by
      a small dummy chunk. */
   i = 0;
   while (i < i_count)
   {
      apc_chunks[i] = heapmgr_malloc((size_t)(((size_t)i * i_size / i_count) + 1));
      ASSURE((i == 0) || (apc_chunks[i] != NULL));

      #ifndef NDEBUG
      {
         /* Fill the newly allocated chunk with some character.
            The character is derived from the last digit of i_rand.
            So later, given i_rand, we can check to make sure that
            the contents haven't been corrupted. */
         size_t i_col;
	      size_t max = ((size_t)i * i_size / i_count) + 1;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < max; i_col++)
            apc_chunks[i][i_col] = c;
      }
      #endif
      i++;
      apc_chunks[i] = heapmgr_malloc((size_t)1);
      i++;
   }

   /* Free the non-dummy chunks in reverse order.  Thus a heapmgr
      implementation that uses a single linked list will be in a
      worst-case state:  the list will contain chunks in increasing
      order by size. */
   i = i_count;
   while (i >= 2)
   {
      i--;
      i--;
      #ifndef NDEBUG
      {
         /* Check the chunk that is about to be freed to make sure
            that its contents haven't been corrupted. */
         size_t i_col;
	      size_t max = ((size_t)i * i_size / i_count) + 1;
         char c = (char)((i % 10) + '0');
         for (i_col = 0; i_col < max; i_col++)
            ASSURE(apc_chunks[i][i_col] == c);
      }
      #endif
      heapmgr_free(apc_chunks[i]);
   }

   /* Allocate chunks in decreasing order by size, thus maximizing the
      amount of list traversal required. */
   i = i_count;
   while (i >= 2)
   {
      i--;
      i--;
      apc_chunks[i] = heapmgr_malloc((size_t)(((size_t)i * i_size / i_count) + 1));
      ASSURE(apc_chunks != NULL);
   }

   /* Free all chunks. */
   for (i = 0; i < i_count; i++)
      heapmgr_free(apc_chunks[i]);
}