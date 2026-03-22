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
    tabuleiro[linha][coluna]=jogador
    if jogador =='X':
        return 'O'
    else:
        return 'X'

jogador=jogada(1,1)
jogador=jogada(1,2)

exibeTabuleiro()


"""Uma outra forma de fazer utilizando o for"""
# tabuleiro=[['' for _ in range(3)] for _ in range(3)]
# print(tabuleiro)