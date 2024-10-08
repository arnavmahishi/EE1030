#include <stdio.h>
#include <math.h>

// Function to solve the quadratic equation ax^2 + bx + c = 0
int solveQuadratic(double a, double b, double c, double *x1, double *x2) {
    double discriminant = b * b - 4 * a * c;
    if (discriminant < 0) {
        return 0; // No real roots
    } else if (discriminant == 0) {
        *x1 = *x2 = -b / (2 * a);
        return 1; // One real root
    } else {
        *x1 = (-b + sqrt(discriminant)) / (2 * a);
        *x2 = (-b - sqrt(discriminant)) / (2 * a);
        return 2; // Two real roots
    }
}

int main() {
    // The line equation x/3 + y/2 = 1 rearranged as y = 2 - (2/3)x
    // Substitute this into the ellipse equation x^2/9 + y^2/4 = 1
    // We end up with a quadratic equation in terms of x
    double a = 1.0 / 9.0 + (4.0 / 9.0);  // Coefficient of x^2
    double b = -(8.0 / 3.0);              // Coefficient of x
    double c = 3.0;                       // Constant term

    // Solve the quadratic equation
    double x1, x2;
    int num_solutions = solveQuadratic(a, b, c, &x1, &x2);

    // Open the file to write the results
    FILE *file = fopen("intersection_points.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    if (num_solutions == 0) {
        fprintf(file, "No intersection points.\n");
    } else {
        // Calculate the corresponding y values for each x
        double y1 = 2 - (2.0 / 3.0) * x1;
        double y2 = 2 - (2.0 / 3.0) * x2;

        // Write both points to the file
        fprintf(file, "Intersection points:\n");
        fprintf(file, "x1 = %lf, y1 = %lf\n", x1, y1);
        if (num_solutions == 2) {
            fprintf(file, "x2 = %lf, y2 = %lf\n", x2, y2);
        }
    }

    fclose(file);
    printf("Intersection points stored in 'intersection_points.txt'.\n");
    return 0;
}

