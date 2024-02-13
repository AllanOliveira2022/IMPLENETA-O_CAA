import heapq

def dijkstra(grafo, inicio):
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0

    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[no_atual]:
            continue

        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias

grafo_exemplo = {
  'A': {'B': 5, 'C': 3, 'D': 2},
  'B': {'A': 5, 'C': 2, 'E': 4},
  'C': {'A': 3, 'B': 2, 'D': 1},
  'D': {'A': 2, 'C': 1, 'E': 7},
  'E': {'B': 4, 'D': 7}
}

no_inicial = 'B'
resultado = dijkstra(grafo_exemplo, no_inicial)

for destino, distancia in resultado.items():
    print(f"Caminho mais curto de {no_inicial} para {destino}: {distancia}")
