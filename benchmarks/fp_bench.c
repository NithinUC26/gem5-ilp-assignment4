#include <stdio.h>
#define N 200000
int main(void) {
    double a = 1.0, b = 2.0, c = 3.0, d = 4.0;
    for (int i = 0; i < N; i++) {
        a = a * 1.0000001 + 0.5;
        b = b * 1.0000002 + 0.25;
        c = c * 0.9999999 + 0.125;
        d = d * 1.0000003 + 0.0625;
    }
    printf("fp checksum: %f\n", a + b + c + d);
    return 0;
}
