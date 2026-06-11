#include <stdio.h>

// Ascendente - iterativo (de F(0) hacia F(n))
int fibonacci_asc(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    if (n == 1) return 1;

    int a = 0, b = 1, c;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return b;
}

// Descendente - recursivo (de F(n) hacia F(0))
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

    printf("Ascendente:  Fibonacci(%d) = %d\n", n, fibonacci_asc(n));
    printf("Descendente: Fibonacci(%d) = %d\n", n, fibonacci_desc(n));

    return 0;
}