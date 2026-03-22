perguntas=[['Seu animal gosta de bananas?','macaco']]

while True:
    print('Pense em uma animal...')

    acertou=False
    for pergunta in perguntas:
        resposta=input(f'{pergunta[0]} (s/n): ')
        if resposta.lower()=='s':
            print(f'Voce pensou em {pergunta[1]}!')
            acertou=True
            break
    
    if not acertou:
        animal=input('Desisto! Em qual animal voce pensou? ')
        novapergunta=input('qual pergunta voce faria para diferenciar esse animal? ')
        perguntas.append([novapergunta,animal])

    resposta=input('Quer jogar novamente? (s/n): ')
    if resposta.lower() != 's':
        print('Ok! Foi bom jogar com voce!')
        break




# print('Pense em uma animal...')

# resposta=input('Seu animal gosta de bananas? (s/n): ')
# if resposta.lower()=='s':
#     print('Voce pensou em macaco!')
# else:
#     print('Puxa! Nao connsegui adivinhar!')