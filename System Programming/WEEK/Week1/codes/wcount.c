#include <stdio.h>
#include <ctype.h>
#include <assert.h>

enum DFAState {IN, OUT};
/* count and print the number of words in input */
int main(void) 
{
   int c, nWords = 0;  enum DFAState state = OUT;

   while ((c = getchar()) != EOF) {    
      switch (state) {
         case IN:
		if (isspace(c)) state = OUT;
           	break;
         case OUT:
		if (!isspace (c)) { state = IN; nWords++;}
		break;
         default:
		assert(0);  /* error */ 
 		break;
          }
    }
    printf("# of words: %d\n", nWords); 
    return 0;
}