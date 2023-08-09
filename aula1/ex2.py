def bicolorable_bfs(grafo, no_inicial, cor):
    visitar = [no_inicial]
    cor[no_inicial] = 0  # Atribui a primeira cor ao nó inicial

    while visitar:
        no_atual = visitar.pop(0)

        for vizinho in grafo.get(no_atual, []):
            if cor[vizinho] == -1:
                # Atribui a cor oposta ao vizinho
                cor[vizinho] = 1 - cor[no_atual]
                visitar.append(vizinho)
            elif cor[vizinho] == cor[no_atual]:
                return False  # O grafo não pode ser bicolorido se nós adjacentes têm a mesma cor

    return True

def bicolorable_dfs(grafo, no_atual, cor_atual, cor):
    cor[no_atual] = cor_atual

    for vizinho in grafo.get(no_atual, []):
        if cor[vizinho] == -1:
            if not bicolorable_dfs(grafo, vizinho, 1 - cor_atual, cor):
                return False
        elif cor[vizinho] == cor_atual:
            return False

    return True

def main():
    while True:
        n = int(input())
        if n < 1 or n > 200:
            print("NOT BICOLORABLE.")
            break

        l = int(input())
        arestas = []
        for _ in range(l):
            a, b = map(int, input().split())
            arestas.append((a, b))
        
        grafo = {}
        #Construção grafo não-direcionado
        for a, b in arestas:
            if a not in grafo:
                grafo[a] = []
            if b not in grafo:
                grafo[b] = []
            grafo[a].append(b)
            grafo[b].append(a)
        
        cores = [-1] * n
        
        if bicolorable_bfs(grafo, 0, cores) and bicolorable_dfs(grafo, 0, 0, cores): 
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

if __name__ == "__main__":
    main()
