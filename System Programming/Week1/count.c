#include <stdio.h>
#include <ctype.h>
int main(void) 
{
   int c;  
   int alphaCount  = 0;  
   int digitCount  = 0;  
   int othersCount = 0;     
  
   while ((c = getchar()) != EOF) {    
       if (isalpha(c))      
           alphaCount++;    
       else if (isdigit(c))      
            digitCount++;    
       else      
            othersCount++;  
    }  
    printf("# of alphabets: %d\n", alphaCount);  
    printf("# of digits: %d\n", digitCount);  
    printf("# of other characters: %d\n", othersCount);    
    
    return 0;
}