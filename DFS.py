
class Grafo:
    """_summary_()
    Una clase para representar un objeto gráfico
    Se define un constructor que recibe una lista de bordes y una lista de nodos
    Al definir la lista de nodos, se define una lista de listas de adyacencia
    Se agregan bordes al gráfico no dirigido, es decir, se agrega una arista. 
    Al agregar la arista, se agrega el nodo de destino a la lista de adyacencia del nodo de origen.
    """
    def __init__(self, bordes, nodos):
        self.lista_adyasencia = [[] for _ in range(nodos)]
        for (busqueda, destino) in bordes:# agrega bordes al gráfico no dirigido
            self.lista_adyasencia[busqueda].append(destino)
            self.lista_adyasencia[destino].append(busqueda)

def DFS(grafo, Punto2, vertice_Visitado, parada, nodo_Prinicipal, tiempo, conexion):
    """_summary_
        Realiza DFS en el grafo comenzando desde el vértice denominado "Punto2" y encuentra todos los puentes en el proceso
        
        --------------------------------------------------------------------------------
        Función para buscar un camino en el grafo, se definen diferentes tipos de parametros para buscar un camino.
        Dentro de este se establece el tipo de busqueda, se define una lista de nodos visitados, se define una lista de nodos a visitar.
        Al establecer el tiempo de llegada del nodo, se incrementa haciendo una suma de 1 al tiempo de llegada del nodo.
        Se marca el nodo como visitado, se agrega el nodo a la lista de visitados.
        
        --------------------------------------------------------------------------------------------------------------------
        Se forma un borde entre los nodos visitados(Punto1 y Punto2), se agrega el nodo de destino a la lista de adyacencia del nodo de origen.
        Los vertices que se encuentran en el camino se marcan como visitados. Si un vertice se encuentrra visitado, este no es un borde posterior
        que comienza el siguiente nodo.
        Si el valor de "tiempo_Llegada", permance sin cambios, siendo igual al tiempo de llegada del vertice del Punto2. Esto forma un puente entre los vertices.
        Devolviendo el valor de "tiempo_Llegada" del vertice que se agrego el vertice.
        
        Returns:
            _type_: _description_
    """
    
    tiempo = tiempo + 1
    parada[Punto2] = tiempo
    vertice_Visitado[Punto2] = True
    
    tiempo_Llegada = parada[Punto2]

    for Punto1 in grafo.lista_adyasencia[Punto2]:

        if not vertice_Visitado[Punto1]:
            tiempo_Llegada = min(tiempo_Llegada, DFS(grafo, Punto1, vertice_Visitado, parada, Punto2, tiempo, conexion))

        elif Punto1 != nodo_Prinicipal:
            tiempo_Llegada = min(tiempo_Llegada, parada[Punto1])

    if tiempo_Llegada == parada[Punto2] and nodo_Prinicipal != -1:
        conexion.add((nodo_Prinicipal, Punto2))
    return tiempo_Llegada

def conexion_Encontrada(grafo, nodos):
    """_summary_
        Se implementa un metodo de la conexion que se genera en los vertices. 
        Para esto se realiza un seguimiento de los vertices que se encuentran en el camino(se visitia o no se visita).
        Se almace el tiepo de llegada "parada = [None] * nodos" en el vertice que se encuentra en el camino.
        Cuando el nodo principal es -1, se define el nodo principal como el vertice que se encuentra en el camino.
        Y el grafo daod se conecta, cubriendo el recorrido de todos los nodos.
    Args:
        grafo (_type_): _description_
        nodos (_type_): _description_

    Returns:
        _type_: _description_
    """
    vertice_Visitado = [False] * nodos
    parada = [None] * nodos
    inicio = 0
    nodo_Prinicipal = -1
    tiempo = 0
    conexion = set()

    DFS(grafo, inicio, vertice_Visitado, parada, nodo_Prinicipal, tiempo, conexion)
    return conexion

if __name__ == '__main__':
    
    # Se representa los pares ordenados de los bordes del grafo 
    bordes = [(1,2),
            (1,3),
            (2,13),
            (2,14),
            (3,4),
            (4,5),
            (5,6),
            (5,7),
            (6,8),
            (6,12),
            (7,13),
            (7,12),
            (12,8),
            (12,11),
            (8,9),
            (9,10),
            (10,11),
            (9,26),
            (9,24),
            (24,25),
            (24,23),
            (11,17),
            (12,16),
            (13,16),
            (14,18),
            (14,15),
            (15,18),
            (19,20),
            (18,20),
            (16,19),
            (16,21),
            (20,21),
            (17,21),
            (23,22),
            (25,22),
            (22,21),
            (3,13),
            (15,16),
            (15,13),
            (25,10),
            (25,17)
            ]
    nodos = 26 #número total de nodos de paradas en el gráfo (0 a 2)

    grafo = Grafo(bordes, nodos) #Representa el grafo de construccion

    conexion = conexion_Encontrada(grafo, nodos)
    if conexion:
        print('La conexion del Recorrido DFS es', conexion)
    else:
        print('El grafo se conecta por 2 aristas') 
