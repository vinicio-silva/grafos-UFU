def find_adjacent_pockets(grid, row, col):
    # Função para encontrar pockets adjacentes a partir de uma posição (row, col)
    # Retorna uma lista de posições adjacentes
    
    adjacent_positions = []
    
    # Possíveis movimentos (horizontal, vertical e diagonal)
    moves = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1), (1, 0), (1, 1)]
    
    for dr, dc in moves:
        newRow, newCol = row + dr, col + dc
        # Verificar se existe a linha e a coluna adjacente no grid e se é pocket de petróleo
        if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == '@':
            adjacent_positions.append((newRow, newCol))
    
    return adjacent_positions

def explore_deposit(grid, row, col):
    # Função para explorar um depósito a partir de uma posição (row, col)
    # Marca o depósito como visitado e explora os pockets adjacentes
    
    grid[row][col] = '*'  # Marca com '*' os pockets de petróleo adjacentes visitados
    adjacent_pockets = find_adjacent_pockets(grid, row, col)
    
    for adj_row, adj_col in adjacent_pockets:
        if grid[adj_row][adj_col] == '@':
            # Recursão para visitar todos os pockets adjacentes possíveis
            explore_deposit(grid, adj_row, adj_col)

def count_oil_deposits(grid):
    # Função para contar o número de depósitos de petróleo em um grid    
    num_deposits = 0    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                num_deposits += 1
                explore_deposit(grid, row, col)
    
    return num_deposits

def main():
    while(True):
        # Lê os valores de m e n na mesma linha
        m, n = map(int, input().split())
        if m == 0 or n == 0:
            print("Fim da execução")
            break
        # Verifica se os valores estão dentro das restrições
        if 1 <= m <= 100 and 1 <= n <= 100:   
            grid = []         
            for _ in range(m):
                linha = input()
                if len(linha) != n:
                    print("Largura da linha é: ", n)
                    break 
                if any(caracter not in ['@', '*'] for caracter in linha):
                    print("Caracteres permitidos da linha são @ e *: ")
                    break 
                grid.append(list(linha))
                
            num_deposits = count_oil_deposits(grid)
            print(num_deposits)
        else:
            print("Erro: 1 ≤ m ≤ 100 and 1 ≤ n ≤ 100")            
            break     

if __name__ == "__main__":
    main()
