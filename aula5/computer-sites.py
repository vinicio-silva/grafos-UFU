class Grafo:
    def __init__(self):
        self.adj = {}  # Dicionário para armazenar listas de adjacência

    def add_aresta(self, v1, v2, custo):
        if v1 not in self.adj:
            self.adj[v1] = {}  # Cria vertice v1
        if v2 not in self.adj:
            self.adj[v2] = {}  # Cria vertice v2
            
        self.adj[v1][v2] = custo  # Cria aresta v1-v2 e atribui um custo
        self.adj[v2][v1] = custo  # Cria aresta v2-v1 e atribui um custo

    def find(self, v, parent):
        if parent[v] == -1: # Verifica se é raiz do conjunto
            return v 
        return self.find(parent[v], parent)

    def union(self, v1, v2, parent):
        raiz_v1 = self.find(v1, parent)
        raiz_v2 = self.find(v2, parent)
        parent[raiz_v1] = raiz_v2 # União dos dois conjuntos

    def calcular_mst(self):
        mst = [] # Arestas da árvore geradora mínima
        arestas = [] # Armazenar arestas do grafo
        parent = {} # Armazenar os conjuntos distuntos

        for v1 in self.adj:
            parent[v1] = -1  # Inicialize o conjunto disjunto para cada vértice (raiz)
            for v2, custo in self.adj[v1].items():
                arestas.append((v1, v2, custo))

        arestas.sort(key=lambda x: x[2]) # Arestas em ordem crescente de custo

        for aresta in arestas: # Itera as arestas
            v1, v2, custo = aresta
            conjunto_v1 = self.find(v1, parent)
            conjunto_v2 = self.find(v2, parent)

            if conjunto_v1 != conjunto_v2: # Verifica se v1 e v2 estão em conjuntos diferentes
                mst.append(aresta) # Adiciona a aresta que faz parte da árvore geradora mínima
                self.union(v1, v2, parent) # Une os conjuntos de v1 e v2

        return mst

def main():
    N = int(input()) # Numero de computer sites
    
    grafo1 = Grafo() # Inicialização do grafo
    grafo2 = Grafo()
    
    for _ in range(N-1):
        v1, v2, custo = map(int, input().split()) # Leitura dos linhas e do custo
        grafo1.add_aresta(v1, v2, custo)
        grafo2.add_aresta(v1, v2, custo)           
        
    K = int(input()) # Numero de linhas adicionais
    
    for _ in range(K):
        v1, v2, custo = map(int, input().split()) # Leitura dos linhas e do custo
        grafo2.add_aresta(v1, v2, custo)
    
    M = int(input()) # Numero de linhas originais
    
    for _ in range(M):
        v1, v2, custo = map(int, input().split()) # Leitura dos linhas e do custo
        grafo2.add_aresta(v1, v2, custo)
    
    mst1 = grafo1.calcular_mst()
    custo_inicial = sum(aresta[2] for aresta in mst1)
    
    mst2 = grafo2.calcular_mst()
    custo_final = sum(aresta[2] for aresta in mst2)
    
    print(custo_inicial)
    print(custo_final)
    
if __name__ == "__main__":
    main()
