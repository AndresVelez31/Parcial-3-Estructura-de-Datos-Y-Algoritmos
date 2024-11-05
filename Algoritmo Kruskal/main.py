class UnionFind:
    def __init__(self, vertices):
        """
        Inicializa la estructura Union-Find.

        Parámetros:
        vertices (iterable): Lista de nodos en el grafo.
        """
        self.padre = {v: v for v in vertices}
        self.rango = {v: 0 for v in vertices}

    def encontrar(self, v):
        """
        Encuentra el representante del conjunto al que pertenece el nodo v.

        Parámetros:
        v: Nodo cuyo representante se desea encontrar.

        Retorna:
        El representante del conjunto.
        """
        if self.padre[v] != v:
            self.padre[v] = self.encontrar(self.padre[v])  # Compresión de caminos
        return self.padre[v]

    def unir(self, u, v):
        """
        Une los conjuntos a los que pertenecen los nodos u y v.

        Parámetros:
        u, v: Nodos cuyos conjuntos se desean unir.

        Retorna:
        True si los conjuntos fueron unidos, False si ya estaban en el mismo conjunto.
        """
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)

        if raiz_u == raiz_v:
            return False  # Ya están en el mismo conjunto

        # Unión por rango
        if self.rango[raiz_u] < self.rango[raiz_v]:
            self.padre[raiz_u] = raiz_v
        else:
            self.padre[raiz_v] = raiz_u
            if self.rango[raiz_u] == self.rango[raiz_v]:
                self.rango[raiz_u] += 1
        return True

def kruskal(grafo):
    """
    Encuentra el Árbol Generador Mínimo de un grafo no dirigido y ponderado.

    Parámetros:
    grafo (list): Lista de aristas con pesos, donde cada arista es una tupla (u, v, peso).

    Retorna:
    list: Lista de aristas que forman el AGM.
    """
    # Ordenar las aristas por peso ascendente
    aristas = sorted(grafo, key=lambda x: x[2])

    # Obtener todos los nodos del grafo
    vertices = set()
    for arista in grafo:
        vertices.update([arista[0], arista[1]])

    # Inicializar la estructura Union-Find
    union_find = UnionFind(vertices)

    agm = []
    for arista in aristas:
        u, v, peso = arista
        # Si u y v están en diferentes conjuntos, unirlos y añadir la arista al AGM
        if union_find.unir(u, v):
            agm.append(arista)

    return agm

# Ejemplos de uso y pruebas de validación
if __name__ == "__main__":
    def imprimir_agm(agm):
        print("Aristas del Árbol Generador Mínimo:")
        for arista in agm:
            print(f"{arista[0]} - {arista[1]} con peso {arista[2]}")
        print(f"Peso total del AGM: {sum([arista[2] for arista in agm])}\n")

    # Ejemplo 1: Grafo Conectado con Ciclo
    print("### Ejemplo 1: Grafo Conectado con Ciclo ###")
    grafo1 = [
        (1, 2, 4),
        (1, 3, 3),
        (2, 4, 2),
        (3, 4, 5)
    ]
    agm1 = kruskal(grafo1)
    imprimir_agm(agm1)
    # Salida Esperada:
    # Aristas del Árbol Generador Mínimo:
    # 2 - 4 con peso 2
    # 1 - 3 con peso 3
    # 1 - 2 con peso 4
    # Peso total del AGM: 9

    # Ejemplo 2: Grafo Desconectado (Bosque Generador Mínimo)
    print("### Ejemplo 2: Grafo Desconectado ###")
    grafo2 = [
        (1, 2, 1),
        (1, 3, 3),
        (4, 5, 2),
        (5, 6, 4)
    ]
    agm2 = kruskal(grafo2)
    imprimir_agm(agm2)
    # Salida Esperada:
    # Aristas del Árbol Generador Mínimo:
    # 1 - 2 con peso 1
    # 4 - 5 con peso 2
    # 1 - 3 con peso 3
    # 5 - 6 con peso 4
    # Peso total del AGM: 10

    # Ejemplo 3: Grafo con Aristas de Mismo Peso
    print("### Ejemplo 3: Grafo con Aristas de Mismo Peso ###")
    grafo3 = [
        (1, 2, 2),
        (1, 3, 2),
        (2, 3, 2),
        (2, 4, 3),
        (3, 4, 3)
    ]
    agm3 = kruskal(grafo3)
    imprimir_agm(agm3)
    # Salida Esperada:
    # Aristas del Árbol Generador Mínimo:
    # 1 - 2 con peso 2
    # 1 - 3 con peso 2
    # 2 - 4 con peso 3
    # Peso total del AGM: 7
