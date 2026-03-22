print('Ola, eu sou a sua assistente, Pytrina. O que voce quer fazer hoje?')

comando=input('Digite um comando: ')

match comando:
    case 'oi'|'ola':
        print('Oi, como vai voce?')
    case 'tchau'|'sair'|'fim'|'exit':
        print('Tchau, foi bom conversar com voce!')
    case 'piada':
        print('Sabe qual eh o padroeiro das pessoas que trabalham com TI? O Sao Login')
    case 'clima'|'previsao do tempo':
        print('Esta muito quente!! Deve ter passado de 40 graus! 🥵')
    case _:
        print('Desculpe, nao entendi o comando')