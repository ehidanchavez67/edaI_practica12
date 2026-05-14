#include <stdio.h>
int fibonacci(int n) {
    int a = 0, b = 1, c;

    if (n == 0)
        return 0; // caso base 

    for (int i = 2; i <= n; i++) { // El for convierte al programa en forma iterativa
        c = a + b;
        a = b;
        b = c;
    }

    return b;
}

int main() {
    int n;

    printf("Ingresa un numero entero: ");
    scanf("%d", &n);

    printf("Fibonacci(%d) = %d\n", n, fibonacci(n));

    return 0;
}
