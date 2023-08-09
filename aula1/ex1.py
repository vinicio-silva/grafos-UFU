class Grafo:
    def __init__(self, num_nos):
        self.grafo = {}
        for i in range(num_nos):
            self.grafo[i] = []
        
    def insere_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
        
def dfs(grafo, no, visitado, divida):
    visitado[no] = True
    divida_total = divida[no]
    
    for vizinho in grafo[no]:
        if not visitado[vizinho]:
            divida_total += dfs(grafo, vizinho, visitado, divida)
            
    return divida_total


def main():
    try:
        # Lê os valores de N e M na mesma linha
        N, M = map(int, input().split())
        
        # Verifica se os valores estão dentro das restrições
        if 2 <= N <= 10000 and 0 <= M <= 50000:            
            # Lê os valores das dívidas em N linhas
            dividas = []
            for _ in range(N):
                num = int(input())
                if -10000 <= num <= 10000:
                    dividas.append(num)
                else:
                    print("IMPOSSIBLE")
                    return 
                                    
            grafo = Grafo(N)
            # Lê os pares de valores X e Y em M linhas
            for _ in range(M):
                X, Y = map(int, input().split())
                if 0 <= X < Y <= N - 1:
                    grafo.insere_aresta(X,Y)
                else:
                    print("IMPOSSIBLE")
                    return                     
                
            visitado = [False] * N
            
            for no in range(N):
                if not visitado[no]:
                    divida_total = dfs(grafo.grafo, no, visitado, dividas)
                    if divida_total != 0:
                        print("IMPOSSIBLE")
                        return                         
            print("POSSIBLE")
            return 
        else:
            print("IMPOSSIBLE")
            return             
    except ValueError:
        print("IMPOSSIBLE")
        return        

if __name__ == "__main__":
    main()
