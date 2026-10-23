# Simulación de Montecarlo para una inversión para el retiro
#
# Idea: no sabemos cuánto va a ganar la inversión cada año.
# Por eso simulamos muchos futuros posibles con números al azar
# y vemos con cuánto dinero terminamos en cada uno.

import random
import matplotlib.pyplot as plt

# Datos de la inversión
ahorro_inicial = 10000      # dinero con el que empiezo
aportacion_anual = 24000    # dinero que meto cada año
anios = 30                  # años hasta el retiro
rendimiento = 0.08          # en promedio gana 8% al año
riesgo = 0.15               # puede subir o bajar 15%
simulaciones = 1000         # cuántos futuros vamos a simular

resultados = []             # aquí guardamos el dinero final de cada simulación

# Repetimos la simulación muchas veces
for i in range(simulaciones):
    dinero = ahorro_inicial

    # Avanzamos año por año
    for anio in range(anios):
        # El rendimiento de este año sale al azar
        rendimiento_del_anio = random.gauss(rendimiento, riesgo)

        # El dinero crece (o baja) y luego agregamos la aportación
        dinero = dinero * (1 + rendimiento_del_anio)
        dinero = dinero + aportacion_anual

    # Guardamos el resultado de esta simulación
    resultados.append(dinero)

# Calculamos el promedio
promedio = sum(resultados) / simulaciones

# Buscamos el peor y el mejor caso
peor = min(resultados)
mejor = max(resultados)

# Contamos cuántas veces llegamos a la meta
meta = 3000000
veces_que_llegamos = 0
for dinero in resultados:
    if dinero >= meta:
        veces_que_llegamos = veces_que_llegamos + 1

probabilidad = veces_que_llegamos / simulaciones * 100

# Mostramos los resultados
print("Dinero promedio al retiro:", round(promedio))
print("Peor caso:", round(peor))
print("Mejor caso:", round(mejor))
print("Probabilidad de llegar a 3 millones:", round(probabilidad), "%")

# Gráfica de los resultados
plt.hist(resultados, bins=30)
plt.title("Simulación de Montecarlo")
plt.xlabel("Dinero al retiro")
plt.ylabel("Número de simulaciones")
plt.savefig("resultados.png")
plt.show()
