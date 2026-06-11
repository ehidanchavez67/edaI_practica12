def fibonacci_descendente(n):
    if n < 0:
        return "El número debe ser no negativo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_descendente(n - 1) + fibonacci_descendente(n - 2)


def serie_fibonacci_descendente(n):
    return [fibonacci_descendente(i) for i in range(n + 1)]