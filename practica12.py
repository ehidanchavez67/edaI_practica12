import matplotlib.pyplot as plt
from fibonacci_descendente import fib_asc, fib_des
from time import time

tiempo_asc = []
tiempo_des = []

for i in range(1, 41):  # "1" -> "i"
    t0 = time()
    fib_des(i)
    tiempo_des.append(round(time() - t0, 6))  # "apppend" -> "append"

    t0 = time()
    fib_asc(i)
    tiempo_asc.append(round(time() - t0, 6))

datos = list(range(1, 41))  # simplificado

fig, ax = plt.subplots()  # "pit" -> "plt"
ax.plot(datos, tiempo_des, label="fib_des", marker="*", color="r")  # usaba tiempo_asc dos veces
ax.plot(datos, tiempo_asc, label="fib_asc", marker="o", color="g")
ax.set_xlabel("n")
ax.set_ylabel("Tiempo (s)")
ax.set_title("Comparación: Fibonacci ascendente vs descendente")
ax.legend()

plt.tight_layout()
plt.show()import matplotlib.pyplot as plt
from fibonacci_descendente import fib_asc, fib_des
from time import time

tiempo_asc = []
tiempo_des = []

for i in range(1, 41):  # "1" -> "i"
    t0 = time()
    fib_des(i)
    tiempo_des.append(round(time() - t0, 6))  # "apppend" -> "append"

    t0 = time()
    fib_asc(i)
    tiempo_asc.append(round(time() - t0, 6))

datos = list(range(1, 41))  # simplificado

fig, ax = plt.subplots()  # "pit" -> "plt"
ax.plot(datos, tiempo_des, label="fib_des", marker="*", color="r")  # usaba tiempo_asc dos veces
ax.plot(datos, tiempo_asc, label="fib_asc", marker="o", color="g")
ax.set_xlabel("n")
ax.set_ylabel("Tiempo (s)")
ax.set_title("Comparación: Fibonacci ascendente vs descendente")
ax.legend()

plt.tight_layout()
plt.show()

