# Criando uma função que recebe *args (quantidade qualquer de argumentos)
def soma(*args):
    lista = [numero for numero in args]
    return sum(lista)
print(soma(1, 2, 3))

# Outro exemplo
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
print(multiplicacao(2, 5, 10))

# Misturando parâmetros
def apresentar(nome, *apelidos):
    print(nome)
    print(apelidos)
apresentar('Caio', 'Caiao', 'Terror do mineirão', 'Caioba')

# Usando kwargs (parâmetros utilizados como um dicionário)
def criar_usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
criar_usuario(nome='Ana', idade=20, cidade='Uberaba')

# Misturando todos os tipos de parâmetros
def exemplo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
exemplo(10, 20, 30, 40, cor='azul', tamanho='M')

# Usando o operador de desempacotamento
numeros = [1, 2, 3]
print(*numeros)

matriz_numeros = [
    *[1, 2],
    *[3, 4]
]
print(matriz_numeros)

dicionario1 = {
    'termo1': 1
}
dicionario2 = {
    'termo2':  2
}
matriz_dicionario = {
    **dicionario1,
    **dicionario2
}
print(matriz_dicionario)

# Ex 1:
def f(*args):
    print(args)
f(10, 20, 30)

# Ex 2:
def f(**kwargs):
    print(type(kwargs))
f(nome='Caio', idade=19)

# Ex 3:
def maior(*args):
    numeros = [numero for numero in args]
    return max(numeros)
print(maior(9, 18, 100, -1, 4))

# Ex 4:
def f(a, *args):
    print(a)
    print(args)
f(5, 10, 15)

# Desafio:
def exemplo(*args, **kwargs):
    print(args)
    print(kwargs)
exemplo(1, 2, nome='Caio', idade=19)