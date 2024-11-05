class UnionFind:
    def __init__(self, vertices):
        # Inicializa cada nodo como su propio padre y establece el rango en 0
        self.padre = {v: v for v in vertices}
        self.rango = {v: 0 for v in vertices}

    def encontrar(self, v):
        # Encuentra el representante (raíz) del conjunto al que pertenece v
        # Aplica compresión de caminos para optimizar futuras búsquedas
        if self.padre[v] != v:
            self.padre[v] = self.encontrar(self.padre[v])
        return self.padre[v]

    def unir(self, u, v):
        # Encuentra las raíces de u y v
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)

        # Si ya están en el mismo conjunto, no hace falta unirlos
        if raiz_u == raiz_v:
            return False

        # Unión por rango: el conjunto de menor rango se une al de mayor rango
        if self.rango[raiz_u] < self.rango[raiz_v]:
            self.padre[raiz_u] = raiz_v
        else:
            self.padre[raiz_v] = raiz_u
            if self.rango[raiz_u] == self.rango[raiz_v]:
                self.rango[raiz_u] += 1
        return True

def kruskal(grafo):
    # Ordena las aristas por peso ascendente
    aristas = sorted(grafo, key=lambda x: x[2])

    # Obtiene todos los nodos únicos en el grafo
    vertices = set()
    for arista in grafo:
        vertices.update([arista[0], arista[1]])

    # Inicializa Union-Find para manejar conjuntos de nodos
    union_find = UnionFind(vertices)
    agm = []  # Lista que almacenará las aristas del AGM

    # Itera sobre las aristas ordenadas
    for arista in aristas:
        u, v, peso = arista
        # Une los conjuntos de u y v si no forman un ciclo y añade la arista al AGM
        if union_find.unir(u, v):
            agm.append(arista)

    return agm

if __name__ == "__main__":
    def imprimir_agm(agm):
        # Imprime las aristas del Árbol Generador Mínimo y su peso total
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
    # Salida esperada:
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
    # Salida esperada:
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
    # Salida esperada:
    # Aristas del Árbol Generador Mínimo:
    # 1 - 2 con peso 2
    # 1 - 3 con peso 2
    # 2 - 4 con peso 3
    # Peso total del AGM: 7
