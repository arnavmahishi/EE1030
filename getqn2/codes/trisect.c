#include <stdio.h>
#include <math.h>

double distance(double x1, double y1, double x2, double y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

void solve_system(double A[2][2], double b[2], double x[2], int n); // Function prototype

int main() {
    double p[2] = {2, 4};
    double a[2] = {5, 0}; // Assuming k is initially 0
    double b[2] = {0, 7}; // Assuming k is initially 0

    // Form the matrix equation Ax = b
    double A[2][2] = {{a[0] - p[0], a[1] - p[1]},
                     {b[0] - p[0], b[1] - p[1]}};
    double b_vector[2] = {p[0]*p[0] + p[1]*p[1] - a[0]*a[0] - a[1]*a[1],
                         p[0]*p[0] + p[1]*p[1] - b[0]*b[0] - b[1]*b[1]};

    // Solve the matrix equation using Gaussian elimination
    double x[2];
    solve_system(A, b_vector, x, 2);

    // The value of k is x[1]
    double k = x[1];

    // Write the coordinates to a text file
    FILE *fp = fopen("points.txt", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    fprintf(fp, "P: (%.2f, %.2f)\n", p[0], p[1]);
    fprintf(fp, "A: (%.2f, %.2f)\n", a[0], a[1]);
    fprintf(fp, "B: (%.2f, %.2f)\n", b[0], b[1]);

    fclose(fp);
    printf("Points stored in points.txt\n");

    return 0;
}

void solve_system(double A[2][2], double b[2], double x[2], int n) {
    // Forward elimination
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            double factor = A[j][i] / A[i][i];
            for (int k = i; k < n; k++) {
                A[j][k] -= factor * A[i][k];
            }
            b[j] -= factor * b[i];
        }
    }

    // Back substitution
    for (int i = n - 1; i >= 0; i--) {
        x[i] = b[i];
        for (int j = i + 1; j < n; j++) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }
}
