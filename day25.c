#include <stdlib.h>
#include <stdio.h>

// To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075.

#define SIZE (2981 + 3075)

typedef struct {
    int x;
    int y;
} coords;

coords next_coords(int x, int y) {
    coords c;
    if (x == 0 && y == 0) {
        c.x = 0;
        c.y = y + 1;
    }
    else if (y > 0) {
        c.x = x + 1;
        c.y = y - 1;
    }
    else {
        c.x = 0;
        c.y = x + 1;
    }
    return c;
}

int main() {
    /* So, to find the second code (which ends up in row 2, column 1),
     * start with the previous value, 20151125.
     * Multiply it by 252533 to get 5088824049625.
     * Then, divide that by 33554393, which leaves a remainder of 31916031.
     * That remainder is the second code. */

    long **codes = malloc(SIZE * sizeof *codes);
    for (int i = 0; i < SIZE; ++i) {
        codes[i] = malloc(SIZE * sizeof *codes[i]);
    }

    codes[0][0] = 20151125;
    coords c = { 0, 0 };
    do {
        long prev_value = codes[c.y][c.x];
        long next_value = (prev_value * 252533) % 33554393;
        c = next_coords(c.x, c.y);
        // printf("%d %d\n", c.x, c.y);
        codes[c.y][c.x] = next_value;
    } while (c.x != 3074 || c.y != 2980);

    printf("%ld\n", codes[2980][3074]);

    return 0;
}