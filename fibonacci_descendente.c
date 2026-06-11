#include <stdio.h>

int fibonacci_desc(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    if (n == 1) return 1;

    return fibonacci_desc(n - 1) + fibonacci_desc(n - 2);
}

int main() {
    int n;

    printf("Ingresa un numero entero: ");
    scanf("%d", &n);

    int resultado = fibonacci_desc(n);

    if (resultado == -1)
        printf("Error: el número debe ser no negativo.\n");
    else
        printf("Fibonacci(%d) = %d\n", n, resultado);

    return 0;
}