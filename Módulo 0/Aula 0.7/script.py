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