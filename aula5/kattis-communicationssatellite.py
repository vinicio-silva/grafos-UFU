import math

def calcular_distancia(antena1, antena2): # Calcular distância entre 2 antenas
    x1, y1, raio1 = antena1
    x2, y2, raio2 = antena2
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) - (raio1 + raio2)
    return distancia

def kruskal(antenas):
    def find(v):  # Verifica conjunto de um vértice pela raiz
        if parent[v] == v:
            return v
        parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2): # União dos dois conjuntos
        raiz_v1 = find(v1)
        raiz_v2 = find(v2)
        parent[raiz_v1] = raiz_v2     
    
    arestas = []  # Lista de todas arestas no formato (distância, antena1, antena2)
    mst = []  # Arestas da árvore geradora mínima  
    parent = list(range(len(antenas))) # Armazenar os conjuntos distuntos para verificar ciclos

    for i in range(len(antenas)):  # Calcula todas as distancias/arestas
        for j in range(i + 1, len(antenas)):
            distancia = calcular_distancia(antenas[i], antenas[j])
            arestas.append((distancia, i, j))
    
    arestas.sort() # Arestas em ordem crescente de distancia
    
    for aresta in arestas: # Itera as arestas
        distancia, v1, v2 = aresta
        conjunto_v1 = find(v1)
        conjunto_v2 = find(v2)

        if conjunto_v1 != conjunto_v2: # Verifica se v1 e v2 estão em conjuntos diferentes
            mst.append(aresta) # Adiciona a aresta que faz parte da árvore geradora mínima
            union(v1, v2) # Une os conjuntos de v1 e v2

    return mst

def main():
    N = int(input()) # Numero de antenas
    antenas = [] # Armazena todas entradas das arestas
    
    for _ in range(N):
        X, Y, R = map(int, input().split()) # Leitura das coordenadas e do raio 
        antenas.append((X, Y, R))
                
    mst = kruskal(antenas)
    comprimento = sum(aresta[0] for aresta in mst)
    print(comprimento)
    
if __name__ == "__main__":
    main()
