def fibonacci(n):
    if n < 0:
        return "El número debe ser no negativo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    
    return b

def serie_fibonacci(n):
    serie = []
    a, b = 0, 1
    
    for i in range(n + 1):
        if i == 0:
            serie.append(a)
        elif i == 1:
            serie.append(b)
        else:
            c = a + b
            serie.append(c)
            a, b = b, c
    
    return serie

if __name__ == "__main__":
    n = 10
    print(f"F({n}) = {fibonacci(n)}")
    print(f"Serie de Fibonacci hasta F({n}):")
    print(serie_fibonacci(n))
    
    print("\nPruebas:")
    for i in range(11):
        print(f"F({i}) = {fibonacci(i)}")
    

    



