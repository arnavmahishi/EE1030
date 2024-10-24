#include <stdio.h>
#include <math.h>

void find_direction_cosines(double plane_normal[3], double direction_cosines[3]) {
    double magnitude = sqrt(plane_normal[0] * plane_normal[0] + plane_normal[1] * plane_normal[1] + plane_normal[2] * plane_normal[2]);
    direction_cosines[0] = plane_normal[0] / magnitude;
    direction_cosines[1] = plane_normal[1] / magnitude;
    direction_cosines[2] = plane_normal[2] / magnitude;
}

int main() {
    double plane_normal[3] = {6, -3, -2};
    double direction_cosines[3];

    find_direction_cosines(plane_normal, direction_cosines);

    printf("Direction cosines of the normal vector: %.3f, %.3f, %.3f\n", direction_cosines[0], direction_cosines[1], direction_cosines[2]);

    // Store input parameters in a text file
    FILE *file = fopen("plane_data.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(file, "%lf %lf %lf\n", plane_normal[0], plane_normal[1], plane_normal[2]);
    fclose(file);

    return 0;
}
