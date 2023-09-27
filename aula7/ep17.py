from collections import deque

class Grafo:
    def __init__(self):
        self.adj = {}  # Dicionário para armazenar listas de adjacência

    def add_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []  # Adiciona um novo vértice com uma lista vazia de vizinhos

    def add_aresta(self, v1, v2):
        self.adj[v1].append(v2)  # Adiciona uma aresta direcionada de A -> B

    def bfs(self, v):
        fila = deque()
        fila.append((v, 0))  # Tupla (vertice, camada) -> source da novidade é a camada 0
        visitados = set()
        camadas = {}  # Quantidade de nos em cada camada

        while fila:
            vertice, camada = fila.popleft()

            if camada not in camadas:
                camadas[camada] = 1
            else:
                camadas[camada] += 1

            visitados.add(vertice)

            for vizinho in self.adj[vertice]:
                if vizinho not in visitados:
                    fila.append((vizinho, camada + 1))
                    visitados.add(vizinho)

        D = max(camadas, key=camadas.get) # First boom day
        M = camadas[D] # Maximum daily boom size

        return M, D

def main():
    E = int(input())  # Leitura do numero de funcionarios

    grafo = Grafo()  # Inicialização do grafo

    for i in range(E):  # Criando arestas que representam as amizades
        grafo.add_vertice(i)
        amigos = list(map(int, input().split()))
        amigos.pop(0)
        for amigo in amigos:
            grafo.add_aresta(i, amigo)

    T = int(input())  # Leitura do numero de casos

    results = []
    for _ in range(T):
        source = int(input())  # Leitura da fonte das novidades
        M, D = grafo.bfs(source)
        results.append((M, D))

    for M, D in results:
        if D == 0 or M == 0:  # Somente source ouviu a informação
            print(0)
        else:
            print(M, D)

if __name__ == "__main__":
    main()
