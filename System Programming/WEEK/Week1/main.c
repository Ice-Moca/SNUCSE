#include <stdio.h>

void f(int a[10]) {
    printf("Inside f: a = %p\n", (void *)a);
    int b;
    a = &b;
    printf("After reassignment: a = %p\n", (void *)a);
}

int main() {
    int x[10];
    printf("In main: x = %p\n", (void *)x);
    f(x);
    printf("In main: x = %p\n", (void *)x);
    return 0;
}