/*
  This is a code from Lecture 11, yet Slide 21 references this code.
*/

int foo(int arg1, int arg2);

int counter = 1;
static int i;
extern int chksum;

static void bar(int c) { chksum ^= c; }

void main(int argc) {
  int k = argc;

  for (i = 0; i < k; i++) {
    counter += foo(i, k);
  }
  bar(counter);
}
