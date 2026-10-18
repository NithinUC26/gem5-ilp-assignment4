#include <stdio.h>
#define N 300000
int main(void) {
    unsigned x = 2463534242u;
    volatile long taken = 0, not_taken = 0;
    for (int i = 0; i < N; i++) {
        x ^= x << 13; x ^= x >> 17; x ^= x << 5;
        if (x & 1) taken++; else not_taken++;
    }
    printf("branch checksum: %ld %ld\n", taken, not_taken);
    return 0;
}
