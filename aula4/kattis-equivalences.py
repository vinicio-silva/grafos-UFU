class Grafo:
    def __init__(self):
        self.adj = {}  # Dicionário para armazenar listas de adjacência

    def add_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []  # Adiciona um novo vértice com uma lista vazia de vizinhos

    def add_aresta(self, v1, v2):
        if v1 in self.adj and v2 in self.adj:
            self.adj[v1].append(v2)  # Adiciona v2 à lista de vizinhos de v1

def findMinimumEdges(grafo, N):
    grauEntrada = [0 for i in range(N + 1)] # Inicializando array para armazenar graus de entrada
    grauSaida = [0 for i in range(N + 1)] # Inicializando array para armazenar graus de saída
    visited = [0 for i in range(N + 1)] # Inicializando array para armazenar vértices visitados
    
    for v in range(1, N + 1): #
        if visited[v] == 0:
            dfs(v, grafo, visited, grauEntrada, grauSaida) # Chamada da dfs com o primeiro vértice
            
    totalEntrada = sum(grauEntrada[1:])
    totalSaida = sum(grauSaida[1:])
    return max(N - totalEntrada, N - totalSaida) # Quantidade mínima de arestas que precisam ser criadas
    
def dfs(u, grafo, visited, grauEntrada, grauSaida):
    visited[u] = 1

    for v in grafo.adj[u]:  # Atribui 1 ao grau de entrada do vértice v e o grau de saída do vértice u
        grauEntrada[v] = 1
        grauSaida[u] = 1
        
        if (visited[v] == 0):
            dfs(v, grafo, visited, grauEntrada, grauSaida)

def main():
    cases = int(input())
    
    results = []
    
    for _ in range(cases):
        N, M = map(int, input().split()) # Leitura do número de statements e implicações
        
        grafo = Grafo() # Inicialização do grafo

        for i in range(N+1):  # Adicionando os vértices
            grafo.add_vertice(i)
        
        for _ in range(M):  # Criando arestas que representam as implicações
            s1, s2 = map(int, input().split())
            grafo.add_aresta(s1, s2)
            
        results.append(findMinimumEdges(grafo, N)) # Função para achar quatidade de arestas mínima

    for result in results:
        print(result)
if __name__ == "__main__":
    main()
