def olaMundo():
    print('Ola, mundo!')
# olaMundo()

def olaPessoa(nome):
    print(f'Ola, {nome}!')
# olaPessoa('Kazue')

def dobro(numero):
    return numero*2
# print(dobro(5)+2)

def MultiplicaDoisNumeros(a,b=2):
    """Multiplica dois numeros"""
    return a*b
# print(MultiplicaDoisNumeros(3,6))
# print(MultiplicaDoisNumeros(3))
x=5 #variavel global
def soma():
    x=10 #variavel local
    print(x)
    return x+1
soma()
print(x)