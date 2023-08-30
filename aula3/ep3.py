def set_graph(R, C): # Cria o grafo com as informações da quantidade de quartos e dos corredores
    graph = [[] for _ in range(R + 1)]
    for _ in range(C):
        A, B = map(int, input().split()) # Leitura dos corredores
        graph[A].append(B)
        graph[B].append(A)
    return graph

def check_simple_path(graph, queries):
    def dfs(start, end, visited):
        if start == end: # Encontra um caminho e retorna 1 para o count
            return 1  
        visited[start] = True
        total_paths = 0  # Inicializa a variável para contar os caminhos
        for neighbor in graph[start]:
            if not visited[neighbor]:
                total_paths += dfs(neighbor, end, visited) # Chamada recursiva da função incrementando o número de caminhos
        visited[start] = False  # Backtrack, permite ser revisitado no futuro enquanto estiver explorando novos caminhos
        return total_paths
    
    results = []
    for S, T in queries:
        visited = [False] * len(graph) # Inicializa array de visitados
        paths = dfs(S, T, visited)
        if paths == 1: # Simple path
            results.append('Y')
        else: # Ou não tem caminho possível ou tem mais de um caminho
            results.append('N')
    return results



def main():
    while True:
        R, C, Q = map(int, input().split()) # Leitura da quantidade de quartos, corredores e pesquisas
        if R == 0 and C == 0 and Q == 0: # Finaliza o programa
            break
        
        graph = set_graph(R, C) # Inicializa o grafo com os quartos (nós) e lê os corredores (arestas)
        
        queries = []
        for _ in range(Q):
            S, T = map(int, input().split()) # Leitura das pesquisas de caminhos
            queries.append((S, T))
        
        results = check_simple_path(graph, queries)
        for result in results:
            print(result)
        print('-')

if __name__ == "__main__":
    main()
