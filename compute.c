#include <stdio.h>
#include <math.h>

#define H 0.0001

#define STEP 0.01
#define INTERVAL_LEFT -10.00
#define INTERVAL_RIGHT 10.00
double f(double x) {
   
    return exp(-x*x) * sin(x); // example
}

double derivative(double (*func)(double), double x) {
    return (func(x + H) - func(x - H)) / (2.0 * H);
}

int main() {
   
    FILE *file = fopen("data.csv", "w");
    if (file == NULL) {
        printf("Eroare la deschiderea fisierului! [data.csv]\n");
        return 1;
    }

    fprintf(file, "x,f,df\n");
    for (double x = INTERVAL_LEFT;  x <= INTERVAL_RIGHT; x += STEP) {
       
        double fx = f(x); // f(x)
        double dfx = derivative(f, x); // f'(x)

        fprintf(file, "%.9f,%.9f,%.9f\n", x, fx, dfx); //precis err 10^-9
    }

    fclose(file);
    printf("data.csv generat cu succes! [compute.c]\n");
    return 0;
}