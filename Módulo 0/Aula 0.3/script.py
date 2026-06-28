def soma(a, b):
    return a + b
resultado = soma(10, 20)

def mostrar(valor):
    print(valor)
x = 10
mostrar(x)

# Nesse exemplo, a etiqueta x nunca deixou de apontar para o 10, ou seja, ao exibir x, parece que a função não teve efeito. Isso acontece porque a etiqueta que agora aponta para o número 11 é o parâmetro numero.
def aumentar(numero):
    numero += 1
x = 10
aumentar(x)
print(x)

# Já nesse exemplo, como listas são objetos mutáveis, tanto a etiqueta numeros como a etiqueta lista, parâmetro da função, apontam para [1, 2, 3] na memória, ou seja, ao modificar a lista através da função, numeros também se altera
def adicionar(lista):
    lista.append(4)
numeros = [1, 2, 3]
adicionar(numeros)
print(numeros)

# Ao usar o append, modificamos o objeto, portanto, ao exibir x, existe alteração
def f(lista):
    lista.append(10)
x = [1]
f(x)
print(x)

# Nessa caso, a etiqueta x permanece inalterada, enquanto a etiqueta lista é quem é reatribuída, por isso parece que a função não teve efeito
def f(lista):
    lista = [10]
x = [1]
f(x)
print(x)

def quadrado(x):
    return x * x
area = quadrado(8)
media = quadrado(5) + quadrado(7)
print(area, media)

def dobro(x):
    return x * 2
x = 3
dobro(x)
print(x)

# Ex 1:
def f(x):
    x = x + 1
a = 5
f(a)
print(a)

# Ex 2:
def f(lista):
    lista.append(5)
a = [1]
f(a)
print(a)

# Ex 3:
def f(lista):
    lista = [10]
a = [1]
f(a)
print(a)

# Desafio:
def alterar(lista):
    lista.append(100)
    lista = [0]
    lista.append(200)
a = [1]
alterar(a)
print(a)