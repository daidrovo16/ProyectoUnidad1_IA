"""
    Link de github:
    https://github.com/daidrovo16/ProyectoUnidad1_IA.git  
    
    Agente que implementa el algoritmo de busqueda en profundidad, para las paradas de autobuses de la ciudad.
    Para ello, utiliza una estructura de datos para almacenar los nodos visitados, y una lista para almacenar los nodos
    que se van a visitar.    
"""
from collections import deque

# Una clase para representar un objeto gráfico
"""
    Se crea una clase para representar un objeto gráfico. En este caso, las paradas de autobuses de la ciudad. Para esto se utiliza una matriz de enteros.
    La cual representa la matriz de la ciudad.    
"""
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al gráfico no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Realizar DFS iterativo en el gráfico a partir del vértice `v`
def iterativeDFS(graph, v, discovered):
 
    # crea una pila utilizada para hacer DFS iterativo
    stack = deque()
 
    # inserta el nodo de origen en la pila
    stack.append(v)
 
    # Bucle # hasta que la pila esté vacía
    while stack:
        # Extrae un vértice de la pila
        v = stack.pop()
 
        # si el vértice ya está descubierto, ignóralo
        if discovered[v]:
            continue
 
        # llegaremos aquí si el vértice reventado `v` aún no se descubre;
        # imprime `v` y procesa sus nodos adyacentes no descubiertos en la pila
        discovered[v] = True
        print(v, end=' ')

        # do para cada arista (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
 
 
if __name__ == '__main__':
 
    # Lista de bordes de gráficos según el diagrama anterior
    edges = [
        # Se observa los pares de nodos que se conectan, se mostrara un cambio en para las paradas (Se realiza este a partado a modo ejemplo)
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # número total de nodos en el gráfico (etiquetados de 0 a 12)
    n = 13
 
    # construye un gráfico a partir de los bordes dados
    graph = Graph(edges, n)
 
    # para realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * n
 
    # Hacer un recorrido DFS iterativo desde todos los nodos no descubiertos hasta
    # cubre todos los componentes conectados de un gráfico
    for i in range(n):
        if not discovered[i]:
            iterativeDFS(graph, i, discovered)

