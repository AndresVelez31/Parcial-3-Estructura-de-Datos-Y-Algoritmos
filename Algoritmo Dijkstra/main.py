class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, distancia, nodo):
        # Añadir el nuevo elemento al final y reordenar
        self.heap.append((distancia, nodo))
        self._heapify_up(len(self.heap) - 1)

    def pop_min(self):
        if not self.heap:
            return None
        # Intercambiar la raíz con el último elemento, quitar el mínimo y reordenar
        self._intercambiar(0, len(self.heap) - 1)
        min_elemento = self.heap.pop()
        self._heapify_down(0)
        return min_elemento

    def _heapify_up(self, indice):
        padre = (indice - 1) // 2
        if indice > 0 and self.heap[indice][0] < self.heap[padre][0]:
            self._intercambiar(indice, padre)
            self._heapify_up(padre)

    def _heapify_down(self, indice):
        mas_pequeño = indice
        izquierda = 2 * indice + 1
        derecha = 2 * indice + 2

        if izquierda < len(self.heap) and self.heap[izquierda][0] < self.heap[mas_pequeño][0]:
            mas_pequeño = izquierda
        if derecha < len(self.heap) and self.heap[derecha][0] < self.heap[mas_pequeño][0]:
            mas_pequeño = derecha
        if mas_pequeño != indice:
            self._intercambiar(indice, mas_pequeño)
            self._heapify_down(mas_pequeño)

    def _intercambiar(self, i, j):
        # Intercambia correctamente los elementos en las posiciones i y j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0


def dijkstra(grafo, inicio):
    # Inicializar distancias con infinito para todos los nodos excepto el nodo de inicio
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Crear el min-heap e insertar el nodo de inicio con distancia 0
    min_heap = MinHeap()
    min_heap.insert(0, inicio)

    # Conjunto de nodos ya visitados
    visitados = set()

    while not min_heap.is_empty():
        # Extraer el nodo con la menor distancia
        distancia_actual, nodo_actual = min_heap.pop_min()

        # Si ya visitamos este nodo, continuamos
        if nodo_actual in visitados:
            continue

        # Marca el nodo como visitado
        visitados.add(nodo_actual)

        # Para cada vecino del nodo actual
        for vecino, peso in grafo[nodo_actual]:
            # Calcula la distancia tentativa
            distancia_tentativa = distancia_actual + peso

            # Si la distancia tentativa es menor, se actualiza
            if distancia_tentativa < distancias[vecino]:
                distancias[vecino] = distancia_tentativa
                min_heap.insert(distancia_tentativa, vecino)

    return distancias

# Ejemplo de uso
grafo = {
    1: [(2, 4), (3, 1)],
    2: [(1, 4), (3, 2), (4, 5)],
    3: [(1, 1), (2, 2), (4, 8)],
    4: [(2, 5), (3, 8)]
}

distancias = dijkstra(grafo, 1)
print(distancias)
