#include <stdio.h>
#define BUFFER 256

int in_corner(int i, int j, int line_length) {
    return i == 1 && j == 1
    || i == 1 && j == line_length
    || i == line_length && j == 1
    || i == line_length && j == line_length;
}

int main() {
    const int line_length = 100;
    int lights[2][line_length + 2][line_length + 2];
    for (int j = 0; j < line_length + 2; ++j) {
        for (int i = 0; i < line_length + 2; ++i) {
            if (in_corner(i, j, line_length)) {
                lights[0][j][i] = lights[1][j][i] = 1;
            }
            else {
                lights[0][j][i] = lights[1][j][i] = 0;
            }
        }
    }

    char line[BUFFER];
    FILE *input = fopen("day18.txt", "r");
    int line_number = 1;
    while (fgets(line, BUFFER, input)) {
        for (int c = 0; c < line_length; ++c) {
            if (line[c] == '#') {
                lights[0][line_number][c+1] = 1;
            }
            else if (line[c] == '.') {
                lights[0][line_number][c+1] = 0;
            }
            else {
                printf("unrecognised character: %c\n", line[c]);
            }
        }
        ++line_number;
    }

    int old_index = 0;
    int new_index = 1;
    for (int t = 0; t < 100; ++t) {
        for (int j = 1; j <= line_length; ++j) {
            for (int i = 1; i <= line_length; ++i) {
                if (in_corner(i, j, line_length)) continue;

                int neighbours_on = 0;
                for (int y = j - 1; y <= j + 1; ++y) {
                    for (int x = i - 1; x <= i + 1; ++x) {
                        if (y == j && x == i) continue;
                        if (lights[old_index][y][x]) ++neighbours_on;
                    }
                }
                if (lights[old_index][j][i] && neighbours_on < 2 || neighbours_on > 3) {
                    lights[new_index][j][i] = 0;
                }
                else if (neighbours_on == 3) {
                    lights[new_index][j][i] = 1;
                }
                else {
                    lights[new_index][j][i] = lights[old_index][j][i];
                }
            }
        }
        old_index = (old_index + 1) % 2;
        new_index = (new_index + 1) % 2;
    }

    int lights_on = 0;
    for (int j = 1; j <= line_length; ++j) {
        for (int i = 1; i <= line_length; ++i) {
            if (lights[old_index][j][i]) ++lights_on;
        }
    }

    printf("%d\n", lights_on);

    return 0;
}