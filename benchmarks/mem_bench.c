#include <stdio.h>
static int arr[128 * 1024];
int main(void) {
    long s = 0;
    for (int i = 0; i < 128 * 1024; i++) arr[i] = i;
    for (int p = 0; p < 8; p++)
        for (int i = 0; i < 128 * 1024; i++) { arr[i] += p; s += arr[i]; }
    printf("mem checksum: %ld\n", s);
    return 0;
}
