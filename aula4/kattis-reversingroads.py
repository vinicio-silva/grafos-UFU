class Grafo:
    def __init__(self):
        self.adj = {}  # Dicionário para armazenar listas de adjacência

    def add_aresta(self, A, B):
        if A not in self.adj:
            self.adj[A] = []  # Adiciona um novo vértice com uma lista vazia de vizinhos
        if B not in self.adj:
            self.adj[B] = []  # Adiciona um novo vértice com uma lista vazia de vizinhos     
        self.adj[A].append(B) # Adiciona aresta direcionada de A -> B

def countGrauSaida(grafo):
    grauSaida = {loja: 0 for loja in grafo.adj} # Inicializando array para armazenar graus de saída
    visited = {loja: 0 for loja in grafo.adj} # Inicializando array para armazenar vértices visitados
    
    def dfs(u, grafo, visited, grauSaida):
        visited[u] = 1

        for v in grafo.adj[u]:  # Atribui 1 ao grau de saída do vértice u
            grauSaida[u] = 1
            
            if (visited[v] == 0):
                dfs(v, grafo, visited, grauSaida)
        return  

    for v in grafo.adj:
        if visited[v] == 0:
            dfs(v, grafo, visited, grauSaida) # Chamada da dfs com o primeiro vértice
    
    vertice_isolado = []        
    for chave, valor in grauSaida.items(): 
        if valor == 0: # Retorna somente os vértices com grau de saída 0
            vertice_isolado.append(chave)
            
    return vertice_isolado

def countArestaBidirecional(grafo):
    visited = {loja: 0 for loja in grafo.adj} # Inicializando array para armazenar vértices visitados
    arestas = []
    
    def dfs(u, grafo, visited):
        visited[u] = 1

        for v in grafo.adj[u]:  # Incrimenta o grau de saída do vértice u
            if (u in grafo.adj[v] and sorted((v,u)) not in arestas): # Verifica se existe aresta de v para u e aresta de u para v
               arestas.append(sorted((v, u)))
            
            if (visited[v] == 0):
                dfs(v, grafo, visited)
        return  

    for v in grafo.adj:
        if visited[v] == 0:
            dfs(v, grafo, visited) # Chamada da dfs com o primeiro vértice
    
    return arestas   # Retorna as arestas bidirecionais

def verificar_nome(nome):
    if len(nome) < 1 or len(nome) > 20:
        return False

    for caractere in nome:
        if not caractere.isalpha():
            return False

    return True

def main():
    N = int(input())
    if (N <= 0 or N >= 10000):
        return 0
        
    grafo = Grafo() # Inicialização do grafo    
        
    for _ in range(N):  # Criando arestas que representam as implicações
        A, B = input().split()
        if A == B or verificar_nome(A) == False or verificar_nome(B) == False:
            return 0
        grafo.add_aresta(A, B)
    
    okay = (countArestaBidirecional(grafo)) # Função para achar arestas bidirecionais
    avoid = (countGrauSaida(grafo)) # Função para achar vertices com grau de saida 0   

    for item in sorted(okay):
        print('okay ' + item[0] + ' ' + item[1])
        
    for item in sorted(avoid):
        print('avoid ' + item)
    
if __name__ == "__main__":
    main()
