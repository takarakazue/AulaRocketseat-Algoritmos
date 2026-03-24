tabuleiro = [
['','',''],
['','',''],
['','','']
]

jogador='X'
def exibeTabuleiro():
    for linha in tabuleiro:
        """Mesma coisa imprimir de outra forma"""
        # print(f'{linha[0]}|{linha[1]}|{linha[2]}')
        # print('-----')
        print('|'.join(linha))
        print('-'*5)

def jogada(linha,coluna):
    if (
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro [linha][coluna] != ''
    ):
        print('Jogada invalida!')
        return  jogador

# def jogada(linha,coluna):
#     if not 0 <= linha <= 2:
#         print('Jogada invalida!')
#         return  jogador
#     if not 0 <= coluna <= 2:
#         print('Jogada invalida!')
#         return  jogador
#     if tabuleiro [linha][coluna] != '':
#         print('Jogada invalida!')
#         return  jogador
    
    tabuleiro[linha][coluna]=jogador
    # if jogador =='X':
    #     return 'O'
    # else:
    #     return 'X'
    return 'O' if jogador == 'X' else 'X'

# jogador=jogada(1,1)
# jogador=jogada(1,2)
# jogador=jogada(2,2)
# exibeTabuleiro()

while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha=int(input('Digite a linha: '))
        coluna=int(input('Digite a coluna: '))
        jogador=jogada(linha, coluna)
    except IndexError:
        print('Digite valores numericos entre 0 e 2')
    except ValueError:
        print('Os valores devem ser numeros inteiros')
    exibeTabuleiro()

"""Uma outra forma de fazer utilizando o for"""
# tabuleiro=[['' for _ in range(3)] for _ in range(3)]
# print(tabuleiro)