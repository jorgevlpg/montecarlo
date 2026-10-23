import random
import matplotlib.pyplot as plt

// Datos de la inversión
ahorro_inicial = 10000      
aportacion_anual = 24000    
anios_hasta_el_retiro = 30                  
rendimiento = 0.08          
riesgo = 0.15               
simulaciones = 1000         

resultados = []            

// loop de la inversion 
for i in range(simulaciones):
    dinero = ahorro_inicial

    
    for anio in range(anios):
        
        rendimiento_del_anio = random.gauss(rendimiento, riesgo)

       
        dinero = dinero * (1 + rendimiento_del_anio)
        dinero = dinero + aportacion_anual

    
    resultados.append(dinero)


promedio = sum(resultados) / simulaciones

// mejor o peor caso 
peor = min(resultados)
mejor = max(resultados)


meta = 3000000
veces_que_llegamos = 0
for dinero in resultados:
    if dinero >= meta:
        veces_que_llegamos = veces_que_llegamos + 1

probabilidad = veces_que_llegamos / simulaciones * 100


print("Dinero promedio al retiro:", round(promedio))
print("Peor caso:", round(peor))
print("Mejor caso:", round(mejor))
print("Probabilidad de llegar a 3 millones:", round(probabilidad), "%")


plt.hist(resultados, bins=30)
plt.title("Simulación de Montecarlo")
plt.xlabel("Dinero al retiro")
plt.ylabel("Número de simulaciones")
plt.savefig("resultados.png")
plt.show()
