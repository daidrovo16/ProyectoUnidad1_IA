# Una clase para representar un objeto gráfico
class Graph:
 
    # Constructor
    def __init__(self, edges, n):
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al gráfico no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Realiza DFS en el gráfico comenzando desde el vértice `v` y encuentra los puentes
# todos los puentes en el proceso


def DFS(graph, v, visited, arrival, parent, time, bridges):
    # establece el tiempo de llegada del vértice `v`
    time = time + 1
    arrival[v] = time
 
    # marcar vértice como visitado
    visited[v] = True
 
    # inicializa `t` con el tiempo de llegada del vértice `v`
    t = arrival[v]
 
    # (v, w) forma un borde
    for w in graph.adjList[v]:
 
        # si no se visita `w`
        if not visited[w]:
            t = min(t, DFS(graph, w, visited, arrival, v, time, bridges))
 
        # si se visita `w` y `w` no es padre de `v`
        elif w != parent:
            # Si el vértice `w` ya está visitado, no
            # es un borde posterior que comienza con `v`. Tenga en cuenta que como `visitado[u]`
            # ya es cierto, la llegada[u] ya está definida
            t = min(t, arrival[w])
 
    # si el valor de `t` permanece sin cambios, es decir, es igual
    # al tiempo de llegada del vértice `v`, y si `v` no es el nodo raíz,
    # entonces (padre[v] —> v) forma un puente
    if t == arrival[v] and parent != -1:
        bridges.add((parent, v))
 
    # devuelve el tiempo mínimo de llegada
    return t
 
 
def findBridges(graph, n):
 
    # para realizar un seguimiento de si se visita un vértice o no
    visited = [False] * n
 
    # almacena el tiempo de llegada de un nodo en DFS
    arrival = [None] * n
 
    start = 0
    parent = -1
    time = 0
 
    bridges = set()
 
    # Como el gráfico dado está conectado, DFS cubrirá todos los nodos
    DFS(graph, start, visited, arrival, parent, time, bridges)
 
    return bridges
 
 
if __name__ == '__main__':
 
    # (u, v) el triplete representa una arista no dirigida desde el vértice `u` hasta el vértice `v`
    edges = [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)]
 
    # número total de nodos en el gráfico (0 a 6)
    n = 6
 
    # gráfico de construcción
    graph = Graph(edges, n)
 
    bridges = findBridges(graph, n)
    if bridges:
        print('Bridges are', bridges)
    else:
        print('Graph is 2–Edge Connected')
 