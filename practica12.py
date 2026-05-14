from fibonacci_descendente import fib, fib_des,fibonacci_descendente
from time import time 

tiempo_asc =[]
tiempo_des = []
tiempo_rec = []

for 1 in range(1,41):
    t0 = time()
    fib_des(i)
    tiempo_des.apppend (round(time()-t0,6))

    t0 = time()
    fib_asc(i)
    tiempo_asc.append(round(time()-t0,6))

datos= []
for i in range(1,41):
    datos.append(i)

fig, ax = pit.subplots()
ax.plot(datos, tiempo_asc, label="fib_des", marker="*", color="r")
ax.plot(datos, tiempo_asc, label="fib_asc", marker="o", color="g")
ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")


