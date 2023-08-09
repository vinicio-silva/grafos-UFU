def validate_corners(mapa):
    if mapa[0][0] == '>' and mapa[0][-1] == 'v' and mapa[-1][0] == '^' and mapa[-1][-1] == '<': 
        return True
    else:
        return False

def main():
    try:
        x = int(input())
        y = int(input())
        
        mapa = []        
        for _ in range(y):
            linha_mapa = input()
            if len(linha_mapa) != x:
                print("!")
                return 
            mapa.append(list(linha_mapa))
        
        # Caso de mapa de 1 linha
        if y == 1:
            # Verifica primeiro elemento '>', se só tem [".", "*"] no restante da linha e quantidade de tesouro
            if mapa[0][0] == '>' and any(caracter in ['.', '*'] for caracter in linha_mapa[1:]) and linha_mapa.count('*') == 1:
                print("*")
                return
            else:
                print("!")
                return
            
        # Caso de mapa de + de 1 linha
        else:
            # Validar os símbolos de todos os cantos
            if not validate_corners(mapa):
                print("!")
                return   
            # Retirando os cantos para percorrer o mapa
            new_map = mapa
            del new_map[0][0]
            del new_map[0][-1]
            del new_map[-1][0]
            del new_map[-1][-1]
            
            count_tesouro = 0
            
            for linha in new_map:
                # Verificando se só tem [".", "*"]
                if any(caracter not in ['.', '*'] for caracter in linha_mapa):
                    print("!")
                    return
                count_tesouro += linha.count('*')
                
            # Verificando quantidade de tesouro
            if count_tesouro != 1:
                print("!")
                return
        
            print("*")
    except ValueError:
        print("!")

if __name__ == "__main__":
    main()
