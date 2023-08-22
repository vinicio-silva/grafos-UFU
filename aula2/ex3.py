def ordenacao_topologica(grafo):
    grau_entrada = [0] * (len(grafo) + 1)  # Inicializa o array de grau de entrada
    ordem = []  # Inicializa a lista de ordem
    
    # Calcula os graus de entrada de todos os nós
    for u in grafo:
        for v in grafo[u]:
            grau_entrada[v] += 1

    # Inicializa uma fila com nós que possuem grau de entrada 0
    fila = [u for u in grafo if grau_entrada[u] == 0]
    
    while fila:
        u = fila.pop(0)
        ordem.append(u)
        
        # Decrementa o grau de entrada dos nós adjacentes e adiciona à fila se o grau de entrada se tornar 0
        for v in grafo[u]:
            grau_entrada[v] -= 1
            if grau_entrada[v] == 0:
                fila.append(v)

    return ordem

def jogo_pick_up_sticks():
    while True:
        n, m = map(int, input().split())  # Lê o número de palitos e linhas
        
        if n == 0 and m == 0:
            break  # Encerra o loop se n e m forem ambos 0
        
        grafo = {i: [] for i in range(1, n+1)}  # Inicializa um grafo vazio
        
        for _ in range(m):
            a, b = map(int, input().split())  # Lê um par de inteiros
            grafo[a].append(b)  # Adiciona uma aresta direcionada de a para b
        
        ordem = ordenacao_topologica(grafo)  # Realiza a ordenação topológica
        
        if len(ordem) == n:
            # Se for possível ordenar todos os palitos sem levantar outros palitos em cima deles, imprime a ordem
            for palito in ordem:
                print(palito)
        else:
            print("IMPOSSIBLE")

# Chama a função para iniciar o jogo "Pick up sticks"
jogo_pick_up_sticks()
