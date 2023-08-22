class Grafo:
    def __init__(self):
        self.adj = {}
  
    def add_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_aresta(self, v1, v2):
        if v1 in self.adj and v2 in self.adj:
            self.adj[v1].append(v2)

    def __str__(self):
        result = ""
        for vertice, vizinhos in self.adj.items():
            result += f"{vertice}: {' '.join(vizinhos)}\n"
        return result
    
    def tem_ciclo(self, v):
        visitados = set()       # Nós visitados
        pilha_recursao = set()  # Nós da pilha de recursão

        def dfs(v):
            visitados.add(v)            # Marca o nó como visitado
            pilha_recursao.add(v)       # Adiciona o nó à pilha de recursão

            for vizinho in self.adj.get(v, []):  # Itera pelos vizinhos do nó atual
                if vizinho not in visitados:     # Se o vizinho ainda não foi visitado
                    if dfs(vizinho):             # Chama recursivamente a DFS no vizinho, se for encontrado um ciclo, retorna True
                        return True              
                elif vizinho in pilha_recursao:   # Se o vizinho já está na pilha de recursão indica a detecção de um ciclo
                    return True                    

            pilha_recursao.remove(v)   # Remove o nó da pilha de recursão ao retroceder
            return False               # Retorna False, indicando que nenhum ciclo foi encontrado

        return dfs(v)  # Inicia a busca em profundidade a partir do nó 'v' e retorna o resultado


def main():
    num = int(input()) # Número de voos
    g = Grafo()
    
    for _ in range(num):
        cidade1, cidade2 = input().split() # Par de cidades
        # Adicionar as cidades como vértices e cria aresta entre elas
        g.add_vertice(cidade1)
        g.add_vertice(cidade2)
        g.add_aresta(cidade1, cidade2)

    cidades_verificar = []
    while True:
        cidade = input() # Cidades para verificação
        if not cidade:
            break
        cidades_verificar.append(cidade)

    for cidade in cidades_verificar:
        if g.tem_ciclo(cidade):
            print(f"{cidade} safe")
        else:
            print(f"{cidade} trapped")

main()