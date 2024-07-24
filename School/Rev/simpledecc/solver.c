#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *inputFile = fopen("flag.enc", "rb");
    FILE *outputFile = fopen("flag_dec.png", "wb");

    if (inputFile == NULL || outputFile == NULL) {
        perror("Failed to open files");
        exit(EXIT_FAILURE);
    }

    unsigned char buffer[8];
    unsigned char xorKey[4];

    // Diberikan:
    unsigned char firstKey[4] = {0x89, 0x50, 0x4E, 0x47};
    unsigned char secondKey[4] = {0x0D, 0x0A, 0x1A, 0x0A};

    // Generate XOR key
    for (int i = 0; i < 4; i++) {
        xorKey[i] = firstKey[i] ^ secondKey[i];
    }

    // Start decryption
    while (fread(buffer, 1, 8, inputFile) == 8) {
        for (int i = 0; i < 8; i++) {
            buffer[i] ^= xorKey[i % 4];
        }
        fwrite(buffer, 1, 8, outputFile);
    }

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
