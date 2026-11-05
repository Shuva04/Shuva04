#include <stdio.h>

int main(void) {
    int choice;
    double a, b;
    for (;;) {
        printf("\n=== C Calculator ===\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Exit\nChoose: ");
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Exiting.\n");
            return 1;
        }
        if (choice == 0) break;
        if (choice < 1 || choice > 4) {
            printf("Choose an option from 0 to 4.\n");
            continue;
        }
        printf("Enter two numbers: ");
        if (scanf("%lf %lf", &a, &b) != 2) {
            printf("Invalid numbers. Exiting.\n");
            return 1;
        }
        switch (choice) {
            case 1: printf("Result: %.10g\n", a + b); break;
            case 2: printf("Result: %.10g\n", a - b); break;
            case 3: printf("Result: %.10g\n", a * b); break;
            case 4:
                if (b == 0.0) printf("Error: division by zero.\n");
                else printf("Result: %.10g\n", a / b);
                break;
        }
    }
    puts("Goodbye!");
    return 0;
}