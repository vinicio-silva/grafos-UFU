def main():
    strings = []

    while True:
        string = input()
        if string == "#":
            break
        strings.append(string)
    
    # Cria um dicionário para representar o grafo de ordem de sequência
    grafo_sequencia = {char: set() for string in strings for char in string}

    # Preenche o grafo de ordem de sequência com base nas strings de entrada
    for i in range(len(strings) - 1):
        string1, string2 = strings[i], strings[i + 1]
        min_length = min(len(string1), len(string2))
        
        for j in range(min_length):
            if string1[j] != string2[j]:
                grafo_sequencia[string1[j]].add(string2[j])
                break

    # Algoritmo de Warshall para completar o grafo de ordem de sequência
    for k in grafo_sequencia:
        for u in grafo_sequencia:
            for v in grafo_sequencia:
                if v != k and v != u:
                    if u in grafo_sequencia[k] and v in grafo_sequencia[u]:
                        grafo_sequencia[k].add(v)

    # Conta as arestas de entrada em cada nó do grafo
    areastas_entrada = {node: 0 for node in grafo_sequencia}

    for node, neighbors in grafo_sequencia.items():
        for neighbor in neighbors:
            areastas_entrada[neighbor] += 1
    print(areastas_entrada)
    # Ordena as chaves do dicionário com base nas contagens de arestas  de entrada
    sequencia_ordenacao = ''.join(sorted(areastas_entrada, key=areastas_entrada.get))
    
    # Imprime a sequência de ordem
    print(sequencia_ordenacao)

if __name__ == "__main__":
    main()

