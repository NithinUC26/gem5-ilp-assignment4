#include <stdio.h>
#define N 200000
int main(void) {
    unsigned a = 1, b = 2, c = 3, d = 4;
    for (unsigned i = 0; i < N; i++) {
        a = a * 1664525u + 1013904223u + i;
        b = b * 22695477u + 1u + (i << 1);
        c = c * 1103515245u + 12345u + (i >> 1);
        d = d * 69069u + 1u + i;
    }
    printf("int checksum: %u\n", a ^ b ^ c ^ d);
    return 0;
}
