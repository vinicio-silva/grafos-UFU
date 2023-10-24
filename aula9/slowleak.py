import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}

    def adicionar_vertice(self, valor):
        self.vertices.add(valor)
        if valor not in self.arestas:
            self.arestas[valor] = []

    def adicionar_aresta(self, i, j, k):
        self.arestas[i].append((j, k))
        self.arestas[j].append((i, k))

def dijkstra(grafo, origem, max_dist, repair_stations):
    distancia = {vertice: float('infinity') for vertice in grafo.vertices}
    distancia[origem] = 0
    fila = [(0, origem)]
    aux = 0 # Variável para auxiliar a medir o caminho percorrido resetando a cada posto de reparo

    while fila:
        (dist, vertice_atual) = heapq.heappop(fila)

        if dist > distancia[vertice_atual]:   # Distância ignorada
            continue

        for (vizinho, peso) in grafo.arestas[vertice_atual]:
            if peso <= max_dist: # Pneu vai esvaziar no meio do caminho
                nova_dist = distancia[vertice_atual] + peso  # Nova distancia possível                
                if nova_dist < distancia[vizinho] and aux + peso <= max_dist: # Se a nova distancia for menor que a atual distancia do vertice e o aux + peso for menor que a max_dist 
                    aux += peso # Incrementa o aux com o peso
                    if vizinho in repair_stations: # Se o vertice for estação de reparo zera o aux
                        aux = 0
                    distancia[vizinho] = nova_dist # Vertice recebe nova e menor distancia                   
                    heapq.heappush(fila, (nova_dist, vizinho)) # Push na fila
                
    return distancia

def main():
    n, m, t, d = map(int, input().split())  # Leitura dos inputs
    repair_stations = set(map(int, input().split()))  # Leitura das estações de reparo

    grafo = Grafo()
    for i in range(1, n + 1):
        grafo.adicionar_vertice(i)

    for _ in range(m):
        i, j, k = map(int, input().split())  # Leitura das estradas e pesos
        grafo.adicionar_aresta(i, j, k)
    
    distancia = dijkstra(grafo, 1, d, repair_stations) # Calcula o menor caminho considerando as estações de reparo

    if distancia.get(n) is not None and distancia[n] != float('inf'): # Verifica se é possível chegar em casa dentro da distância máxima
        print(distancia[n])
    else:
        print("stuck")

if __name__ == "__main__":
    main()