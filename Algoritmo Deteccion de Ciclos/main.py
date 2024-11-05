def contiene_ciclo(grafo):
    """
    Verifica si un grafo no dirigido contiene un ciclo.

    Parámetros:
    grafo (dict): Diccionario que representa el grafo. Las claves son los nodos y los valores son listas de nodos adyacentes.

    Retorna:
    bool: True si el grafo contiene un ciclo, False en caso contrario.
    """
    visitados = set()

    def dfs(nodo_actual, padre):
        """
        Función auxiliar para realizar DFS y detectar ciclos.

        Parámetros:
        nodo_actual (int/str): Nodo que se está visitando actualmente.
        padre (int/str): Nodo desde el cual se llegó al nodo_actual.

        Retorna:
        bool: True si se detecta un ciclo, False en caso contrario.
        """
        visitados.add(nodo_actual)
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                if dfs(vecino, nodo_actual):
                    return True
            elif vecino != padre:
                # Se ha encontrado un vecino ya visitado que no es el padre, indicando un ciclo
                return True
        return False

    # Iterar sobre todos los nodos para manejar grafos desconectados
    for nodo in grafo:
        if nodo not in visitados:
            if dfs(nodo, None):
                return True
    return False

# Ejemplos de uso y pruebas
if __name__ == "__main__":
    # Ejemplo 1: Grafo Sin Ciclos (Árbol)
    grafo_sin_ciclos = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }
    print("Ejemplo 1 - Grafo Sin Ciclos:", contiene_ciclo(grafo_sin_ciclos))  # Debería devolver False.

    # Ejemplo 2: Grafo Con Ciclo (Triángulo)
    grafo_con_ciclo = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    print("Ejemplo 2 - Grafo Con Ciclo:", contiene_ciclo(grafo_con_ciclo))  # Debería devolver True.

    # Ejemplo 3: Grafo Desconexo con Una Componente Cíclica
    grafo_desconexo = {
        1: [2],
        2: [1],
        3: [4, 5],
        4: [3, 5],
        5: [3, 4]
    }
    print("Ejemplo 3 - Grafo Desconexo con Ciclo:", contiene_ciclo(grafo_desconexo))  # Debería devolver True.

    # Ejemplo 4: Grafo Lineal Sin Ciclo
    grafo_lineal = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['C']
    }
    print("Ejemplo 4 - Grafo Lineal Sin Ciclo:", contiene_ciclo(grafo_lineal))  # Debería devolver False.

    # Ejemplo 5: Grafo Con Ciclo (Cuadrado)
    grafo_cuadrado = {
        'A': ['B', 'D'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['A', 'C']
    }
    print("Ejemplo 5 - Grafo Con Ciclo:", contiene_ciclo(grafo_cuadrado))  # Debería devolver True.
