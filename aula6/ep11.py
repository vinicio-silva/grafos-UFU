def kruskal(grafo):  
    def find(parent, cidade): # Verifica conjunto de um vértice encontrando sua raiz
        if cidade not in parent:
            parent[cidade] = cidade
        elif parent[cidade] != cidade:
            parent[cidade] = find(parent, parent[cidade])
        return parent[cidade]

    def union(parent, cidade1, cidade2): # União dos dois conjuntos
        raiz_cidade1 = find(parent, cidade1)
        raiz_cidade2 = find(parent, cidade2)
        parent[raiz_cidade1] = raiz_cidade2
       
    mst = [] # Arestas da árvore geradora maxima  
    parent = {} # Armazenar os conjuntos distuntos para verificar ciclos
    grafo.sort(key=lambda x: x[2], reverse=True) # Arestas do grafo em ordem decrescente de peso
    
    for cidade1, cidade2, peso in grafo: # Itera sob as arestas do grafo
        raiz_cidade1 = find(parent, cidade1)
        raiz_cidade2 = find(parent, cidade2)
        
        if raiz_cidade1 != raiz_cidade2: # Verifica se a raiz da cidade 1 e a raiz da cidade 2 estão em conjuntos diferentes
            mst.append((cidade1, cidade2, peso)) # Adiciona a aresta que faz parte da árvore geradora mínima
            union(parent, raiz_cidade1, raiz_cidade2) # Une os conjuntos da cidade1 com a cidade 2
    return mst

def criar_lista_adjacencia(grafo):  # Cria lista de adjacencia com os vertices sendo as cidades
    lista_adjacencia = {}
    for cidade1, cidade2, peso in grafo:
        if cidade1 not in lista_adjacencia: # Cria nó para cidade 1
            lista_adjacencia[cidade1] = []
        if cidade2 not in lista_adjacencia: # Cria nó para cidade 2
            lista_adjacencia[cidade2] = []
        lista_adjacencia[cidade1].append((cidade2, peso)) # Criar arestas 
        lista_adjacencia[cidade2].append((cidade1, peso))
    return lista_adjacencia

def dfs(lista_adjacencia, partida, destino, visited, menor_caminho): # DFS para achar menor caminho entre 2 cidades
    visited.add(partida)
    menor_caminho.append(partida) # Adiciona cidade no menor caminho

    if partida == destino:  # Condição de parada
        return menor_caminho

    for vizinho, peso in lista_adjacencia[partida]: 
        if vizinho not in visited: 
            resultado = dfs(lista_adjacencia, vizinho, destino, visited, menor_caminho.copy())
            if resultado:
                return resultado

    return None

def get_maximum_load(grafo, partida, destino):
    mst = kruskal(grafo) # Arvore geradora maxima
    visited = set() # Set de visitados
    lista_adjacencia = criar_lista_adjacencia(mst) # Criar estrutura de lista de adjacencia a partir da mst gerada no kurskal
    menor_caminho = dfs(lista_adjacencia, partida, destino, visited, []) # Chamada da dfs para achar menor caminho dentro da lista de adjacencia

    filtered_arestas = [] # Array de arestas que são contem as cidade do menor caminho

    for cidade1, cidade2, peso in grafo:  # Filtra o grafo apenas com as arestas do menor caminho
        if cidade1 in menor_caminho and cidade2 in menor_caminho:
            filtered_arestas.append((cidade1, cidade2, peso))
            
    menor_peso = float('inf')  # Inicializa com infinito para encontrar o menor valor

    for cidade1, cidade2, peso in filtered_arestas: 
        if peso < menor_peso: # Menor valor é o peso máximo 
            menor_peso = peso
            
    return menor_peso
    
def main():   
    X = 0  # Contador de cenarios
    results = [] # Array para armazenar resultados
           
    while True:        
        N, R = map(int, input().split()) # Leitura do numero de cidades e numero de estradas
        X += 1 # Incrementar o numero do cenario
        
        if N == 0 or R == 0: # Condição de parada
            break
        
        grafo = []
        for _ in range(R):
            c1, c2, peso = input().split() # Leitura das estradas e pesos
            grafo.append((c1, c2, int(peso)))
            
        partida, destino = input().split() # Leitura das cidades de partida e destino
        
        max_load = get_maximum_load(grafo, partida, destino) # Chamada da função para obter peso máximo

        results.append(("Scenario #" + str(X), str(max_load) + " tons")) # Formatação da resposta
        
    for cenario, peso in results: # Print das repostas
        print(cenario)
        print(peso)
        print()
    
if __name__ == "__main__":
    main()
