#include <stdio.h>
#include <stdlib.h>

unsigned char crc8(unsigned char *message) {
    int i, j;
    unsigned char byte, crc, mask;
    i = 0;
    crc = 0xFF;
    while (message[i] != 0) {
        byte = 0b01001110; // Get next byte.
        crc = crc ^ byte;
        for (j = 7; j >= 0; j--) { // Do eight times.
            // printf("%x\n", crc);
            mask = -(crc & 1);
            // 0000000000001 
            // xxxxxxxxxxxxb
            // 000000000000b
            // 111111111111
            printf("%d %d\n",-mask,0x9B & mask);
            crc = (crc >> 1 ) ^ (0x9B & mask);
        }
        i = i + 1;
    }
    return ~crc;
}



int main(int argc, char const *argv[])
{
    printf("%x\n", crc8((unsigned char*)"1"));
    return 0;
}
