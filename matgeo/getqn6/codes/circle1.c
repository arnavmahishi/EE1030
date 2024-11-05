#include <stdio.h>
#include <math.h>

#define MAX_POINTS 3

struct Point {
  double x;
  double y;
};

void printMatrix(const struct Matrix *matrix) {
  for (int i = 0; i < MAX_POINTS; i++) {
    for (int j = 0; j < MAX_POINTS; j++) {
      printf("%.2f ", matrix->data[i][j]);
    }
    printf("\n");
  }
}

void rowReduction(struct Matrix *matrix) {
  for (int i = 0; i < MAX_POINTS - 1; i++) {
    // Check if the pivot element is zero
    if (fabs(matrix->data[i][i]) < 1e-6) {
      printf("Matrix may be singular. Results might be inaccurate.\n");
      return;
    }

    // Eliminate elements below the pivot
    for (int j = i + 1; j < MAX_POINTS; j++) {
      double factor = matrix->data[j][i] / matrix->data[i][i];
      for (int k = 0; k < MAX_POINTS; k++) {
        matrix->data[j][k] -= factor * matrix->data[i][k];
      }
    }
  }
}

void findCenterAndRadius(const struct Point *points, struct Point *center, double *radius) {
  struct Matrix A;

  // Set up matrix A based on point coordinates
  A.data[0][0] = 2 * (points[1].x - points[0].x);
  A.data[0][1] = 2 * (points[1].y - points[0].y);
  A.data[0][2] = points[1].x * points[1].x - points[0].x * points[0].x + points[1].y * points[1].y - points[0].y * points[0].y;
  A.data[1][0] = 2 * (points[2].x - points[0].x);
  A.data[1][1] = 2 * (points[2].y - points[0].y);
  A.data[1][2] = points[2].x * points[2].x - points[0].x * points[0].x + points[2].y * points[2].y - points[0].y * points[0].y;

  // Perform Gaussian Elimination
  rowReduction(&A);

  // Solve for center coordinates
  if (fabs(A.data[1][0]) < 1e-6) {
    printf("Points might be colinear. Results might be inaccurate.\n");
  }
  center->x = -A.data[0][2] / (2 * A.data[0][0]);
  center->y = (-A.data[1][2] - 2 * A.data[1][0] * center->x) / (2 * A.data[1][1]);

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

  // Write the results to a text file (optional)
  // ... (similar to the previous code)

  printf("Center: (%.2f, %.2f)\n", center.x, center.y);
  printf("Radius: %.2f\n", radius);

  return 0;
}
