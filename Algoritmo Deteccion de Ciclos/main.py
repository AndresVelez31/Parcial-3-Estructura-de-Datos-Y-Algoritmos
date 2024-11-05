def contiene_ciclo(grafo):
    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario de listas de adyacencia.")
    
    visitados = set()  # Para llevar un registro de los nodos visitados

    # Función auxiliar para DFS
    def dfs(nodo, padre):
        visitados.add(nodo)
        
        # Recorre todos los vecinos del nodo actual
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                if dfs(vecino, nodo):  # Llamada recursiva al vecino
                    return True
            elif vecino != padre:  # Si el vecino ha sido visitado y no es el padre, hay un ciclo
                return True
        return False

    # Ejecutamos DFS en cada componente conectado del grafo
    for nodo in grafo:
        if nodo not in visitados:  # Si el nodo no ha sido visitado, iniciamos DFS desde él
            if dfs(nodo, None):  # Llamada inicial sin padre (None)
                return True  # Si se detecta un ciclo, se devuelve True

    return False  # Si no se encuentra ningún ciclo, se devuelve False


# Ejemplo original
grafo = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
print("Ejemplo 1 - Grafo sin ciclo:", contiene_ciclo(grafo))  # Debería imprimir False

# Ejemplo 2: Grafo con ciclo simple
grafo_ciclo = {
    1: [2],
    2: [1, 3],
    3: [2, 1]  # Crea un ciclo entre 1-2-3-1
}
print("Ejemplo 2 - Grafo con ciclo:", contiene_ciclo(grafo_ciclo))  # Debería imprimir True

# Ejemplo 3: Grafo acíclico (árbol)
grafo_arbol = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}
print("Ejemplo 3 - Grafo acíclico (árbol):", contiene_ciclo(grafo_arbol))  # Debería imprimir False

# Ejemplo 4: Grafo desconectado con ciclo en una componente
grafo_desconectado_con_ciclo = {
    1: [2],
    2: [1],
    3: [4],
    4: [3, 5],
    5: [4, 3]  # Crea un ciclo entre 3-4-5-3
}
print("Ejemplo 4 - Grafo desconectado con ciclo:", contiene_ciclo(grafo_desconectado_con_ciclo))  # Debería imprimir True

# Ejemplo 5: Grafo con múltiples ciclos
grafo_multiples_ciclos = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2],
    4: [2, 5],
    5: [4, 6],
    6: [5, 2]  # Crea ciclos entre 1-2-3-1 y 2-4-5-6-2
}
print("Ejemplo 5 - Grafo con múltiples ciclos:", contiene_ciclo(grafo_multiples_ciclos))  # Debería imprimir True
