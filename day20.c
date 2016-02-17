#include <stdio.h>
#include <stdlib.h>

int main() {
    int max_houses = 10000000;
    int *houses = malloc(max_houses * sizeof *houses);

    for (int elf = 1; elf < max_houses; ++elf) {
        for (int i = elf; i < max_houses && i < 51 * elf; i += elf) {
            houses[i] += elf * 11;
        }
    }

    for (int i = 1; i < max_houses; ++i) {
        int house = houses[i];
        if (house >= 36000000) {
            printf("house %d: %d\n", i, house);
            break;
        }
    }

    return 0;
}