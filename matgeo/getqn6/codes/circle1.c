#include <stdio.h>
#include <math.h>

#define MAX_POINTS 3

struct Point {
    double x;
    double y;
};

struct Matrix {
    double data[MAX_POINTS][MAX_POINTS];
};

void printMatrix(const struct Matrix *matrix) {
    for (int i = 0; i < MAX_POINTS; i++) {
        for (int j = 0; j < MAX_POINTS; j++) {
            printf("%.2f ", matrix->data[i][j]);
        }
        printf("\n");
    }
}

void multiplyMatrices(const struct Matrix *matrix1, const struct Matrix *matrix2, struct Matrix *result) {
    for (int i = 0; i < MAX_POINTS; i++) {
        for (int j = 0; j < MAX_POINTS; j++) {
            result->data[i][j] = 0;
            for (int k = 0; k < MAX_POINTS; k++) {
                result->data[i][j] += matrix1->data[i][k] * matrix2->data[k][j];
            }
        }
    }
}

void invertMatrix(const struct Matrix *matrix, struct Matrix *inverse) {
    double determinant = matrix->data[0][0] * matrix->data[1][1] - matrix->data[0][1] * matrix->data[1][0];

    if (determinant == 0) {
        printf("Matrix is singular. Cannot be inverted.\n");
        return;
    }

    inverse->data[0][0] = matrix->data[1][1] / determinant;
    inverse->data[0][1] = -matrix->data[0][1] / determinant;
    inverse->data[1][0] = -matrix->data[1][0] / determinant;
    inverse->data[1][1] = matrix->data[0][0] / determinant;
}

void findCenterAndRadius(const struct Point *points, struct Point *center, double *radius) {
    struct Matrix A, B, C, inverseA, result;

    // Set up the matrices A, B, and C
    A.data[0][0] = 2 * (points[1].x - points[0].x);
    A.data[0][1] = 2 * (points[1].y - points[0].y);
    A.data[1][0] = 2 * (points[2].x - points[0].x);
    A.data[1][1] = 2 * (points[2].y - points[0].y);

    B.data[0][0] = points[1].x * points[1].x - points[0].x * points[0].x + points[1].y * points[1].y - points[0].y * points[0].y;
    B.data[1][0] = points[2].x * points[2].x - points[0].x * points[0].x + points[2].y * points[2].y - points[0].y * points[0].y;

    C.data[0][0] = points[0].x;
    C.data[1][0] = points[0].y;

    // Invert matrix A
    invertMatrix(&A, &inverseA);

    // Multiply inverseA and B
    multiplyMatrices(&inverseA, &B, &result);

    // Calculate the center
    center->x = result.data[0][0];
    center->y = result.data[1][0];

    // Calculate the radius
    *radius = sqrt((points[0].x - center->x) * (points[0].x - center->x) + (points[0].y - center->y) * (points[0].y - center->y));
}

int main() {
    struct Point points[MAX_POINTS] = {
        {0, 0},
        {2, 0},
        {0, 2}
    };

    struct Point center;
    double radius;

    findCenterAndRadius(points, &center, &radius);

    // Write the results to a text file
    FILE *fp = fopen("circle_data.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "%.2f, %.2f\n", points[0].x, points[0].y);
    fprintf(fp, "%.2f, %.2f\n", points[1].x, points[1].y);
    fprintf(fp, "%.2f, %.2f\n", points[2].x, points[2].y);
    fprintf(fp, "%.2f, %.2f\n", center.x, center.y);
    fprintf(fp, "%.2f\n", radius);

    fclose(fp);

    printf("Results written to circle_data.txt\n");

    return 0;
}
