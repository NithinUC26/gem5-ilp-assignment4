#include <stdio.h>
#define N 200000
int main(void) {
    unsigned a = 1;
    for (unsigned i = 0; i < N; i++) a = a * 1664525u + 1013904223u + i;
    printf("int1 checksum: %u\n", a);
    return 0;
}
