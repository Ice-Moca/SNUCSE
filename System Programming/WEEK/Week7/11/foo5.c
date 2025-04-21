#include <stdio.h>

void f(void);

int x = 12345;
int y = 12346;

int main()
{
    f();
    printf("x=%d y=%d\n", x, y);
    return 0;
}
