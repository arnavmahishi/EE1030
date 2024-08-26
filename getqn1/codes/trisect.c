#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate the distance between two points
double distance(int x1, int y1, int x2, int y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

int main() {
    int x1 = 7, y1 = -2, x2 = 1, y2 = -5;
    int px = 5, py = -3;

    // Calculate distances between points
    double AB = distance(x1, y1, x2, y2);
    double AP = distance(x1, y1, px, py);
    double PB = distance(px, py, x2, y2);

    // Check if point P is a trisection point
    if (AP == PB && AP == AB / 3) {
        printf("Point P(%d, %d) is one of the trisection points of line segment AB.\n", px, py);
    } else {
        printf("Point P(%d, %d) is not a trisection point of line segment AB.\n", px, py);
    }

    // Create a text file to store coordinates
    FILE *fp = fopen("coordinates.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Write coordinates to the file
    fprintf(fp, "Point A: (%d, %d)\n", x1, y1);
    fprintf(fp, "Point P: (%d, %d)\n", px, py);
    fprintf(fp, "Point B: (%d, %d)\n", x2, y2);

    fclose(fp);

    // Plot the coordinates using a plotting library (e.g., gnuplot, matplotlib)
    // Replace this comment with the appropriate plotting code for your chosen library

    return 0;
}
