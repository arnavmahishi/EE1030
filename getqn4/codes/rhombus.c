#include <stdio.h>

int main() {
    int diagonal1 = 6; // Diagonal along the x-axis
    int diagonal2 = 4; // Diagonal along the y-axis

    // Calculate coordinates of vertices
    int x1 = diagonal1 / 2;
    int y1 = diagonal2 / 2;
    int x2 = -x1;
    int y2 = -y1;

    // Store points in a text file
    FILE *file = fopen("rhombus_points.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "A(%d, %d)\n", x1, y1);
    fprintf(file, "B(%d, %d)\n", x2, y1);
    fprintf(file, "C(%d, %d)\n", x2, y2);
    fprintf(file, "D(%d, %d)\n", x1, y2);

    fclose(file);

    printf("Rhombus points generated and stored in rhombus_points.txt\n");

    return 0;
}
