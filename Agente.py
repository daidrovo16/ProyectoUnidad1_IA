"""
    Link de github:
    https://github.com/daidrovo16/ProyectoUnidad1_IA.git    
    Agente que implementa el algoritmo de paradas de autobuses de la ciudad. 
"""
import random

def display(paradas):
    print(paradas)
    """_summary_
    Se importa la libreria random para generar un numero aleatorio entre 0 y el numero de paradas. La cuales seran las paradas de los autobuses.
    Se defineuna un diplay para mostrar el numero de paradas que se generaron. Este display al tener como argumento las pardas las imprimira, 
    desde la funcion main. Se gnera una matriz de este numero de paradas, las cuales mostraran cuando el autobus llegue a la parada.
    """
paradas = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1]
]
print("Paradas del autobus")
display(paradas)

"""_summary_
    Las variables de control de los autobuses son: x, y. Estas variables controlan la posicion del autobus en la matriz de paradas.
    Estas varibles se inicializan en 0.
    Se opta por implementr un ciclo while para que el autobus se mueva en la matriz de paradas. 
    En este ciclo while se toman las variables de control de los autobuses y se les da el numero de paradas de la matriz.
    En la variable paradas[x][y] se guarda el numero de paradas que se encuentran en la matriz.
    y el random.choice(paradas[x][y]) selecciona una de las paradas de la matriz.
    Al seleccion las paradas se imprime el numero de paradas que se encuentran en la matriz. Y se realiza un incremento de la variable de control de las paradas.
"""
#Variables de control del algoritmo para la solcion del problema.
x =0
y= 0
# x = pasajeros y = paradas
while x < 17:
    while y < 17:
        paradas[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0
print("Antes de detectar las paradas, se deteta los pasajeros que llegan a su destino y suben al bus")
display(paradas)
x =0
y= 0
z=0
"""_summary_
    En las siguiente lineas de codigo se realiza un ciclo while para que el autobus se mueva en la matriz de paradas. 
    Cuando este es mayor a 17, se realiza un reseteo de las variables de control. Se implementa un if el cual toma
    la variable de control de las paradas y si es mayor a 17, se igual a 1. Esto ocurre para el autobus se detenga 
    en la parada generando asi una lista de paradas.
    
    Por ultimo la variable pro se la implementa para mostrar la medida de desempeño del algoritmo.
    Dependiendo de la cantidad de paradas que se encuentran en la matriz, el algoritmo se demora mas o menos. Y mostrara el rendimiento en porcentaje.
"""
while x > 17:
    while y > 17:
        if paradas[x][y] == 1:
            print("Pare en esta ubicacion cuando exista la necesidad,",x, y)
            paradas[x][y] = 0
            print("Parada", x, y)
            z+=1
        y+=1
    x+=1
    y=0
pro= (100-((z/289)*100))
print("Se detectaron pasajeros en las paradas y se quedan en la parada")
display(paradas)
print('Medida de Desempenio=',pro,'%')

