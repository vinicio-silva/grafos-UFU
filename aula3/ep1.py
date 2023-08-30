class Grafo:
    def __init__(self):
        self.adj = {}  # Dicionário para armazenar listas de adjacência

    def add_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []  # Adiciona um novo vértice com uma lista vazia de vizinhos

    def add_aresta(self, v1, v2):
        if v1 in self.adj and v2 in self.adj:
            self.adj[v1].append(v2)  # Adiciona v2 à lista de vizinhos de v1
            self.adj[v2].append(v1)  # Adiciona v1 à lista de vizinhos de v2

    def dfs(self, v, visitados):
        visitados.add(v)
        for vizinho in self.adj[v]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def componentes_conexas(self):
        visitados = set()
        num_componentes = 0
        for vertice in self.adj: #Visita os vértices pela lista de adj
            if vertice not in visitados: #Se um vértice não foi visitado, aumenta a quantidade de componentes
                num_componentes += 1
                self.dfs(vertice, visitados) #Percorre a partir deste novo vértice
        return num_componentes

    def pontos_de_articulacao(self):
        pontos_articulacao = []

        for vertice in self.adj:
            atual = self.componentes_conexas()
            #Cria adjacencia temporaria, removendo um vertice
            temp_adj = {v: [viz for viz in self.adj[v] if viz != vertice] for v in self.adj if v != vertice}
            temp_grafo = Grafo()
            temp_grafo.adj = temp_adj

           #Verifica a quantidade de componentes sem o vertice
            num_componentes_sem_vertice = temp_grafo.componentes_conexas()

            #Se aumentar a quantidade se trata de um ponto de articulacao
            if num_componentes_sem_vertice > atual:
                pontos_articulacao.append(vertice)

        return pontos_articulacao

def main():
    grafos = []

    while True:
        n_cidades = int(input("Quantidade de cidades (0 para sair): "))

        if n_cidades == 0:
            break

        grafo = Grafo()

        for i in range(n_cidades):
            cidade = input(f"Cidade {i+1}: ")
            grafo.add_vertice(cidade)

        n_rotas = int(input("Quantidade de rotas: "))
        for _ in range(n_rotas):
            cidade1, cidade2 = input("Digite os nomes das cidades ligadas por uma rota: ").split()
            grafo.add_aresta(cidade1, cidade2)

        grafos.append(grafo)

    for idx, grafo in enumerate(grafos):
        pontos_articulacao = grafo.pontos_de_articulacao()
        print(f"City Map #{idx + 1}:")

        print(f"{len(pontos_articulacao)} camera(s) found")

        for cidade in pontos_articulacao:
            print(f"{cidade }")

def main():
  grafos = []

  while True:
    grafo = Grafo()
    n_pontos = int (input("Quantidade de pontos: "))
    if n_pontos == 0:
      break

    for i in range(n_pontos):
      grafo.add_vertice(i+1)

    for i in range(n_pontos):
      adj = []
      entrada = list(map(int, input("Pontos: ").split()))
      if entrada[0] == 0:
        break
      vertice = entrada[0]
      adj.extend(entrada[1:])

      for ponto in adj:
        grafo.add_aresta(vertice, ponto)

    grafos.append(grafo)

  for grafo in grafos:
    pontos_articulacao = grafo.pontos_de_articulacao()
    print(len(pontos_articulacao))

main()
