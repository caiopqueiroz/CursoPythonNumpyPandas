# Criando um set 
frutas = {'maçã', 'banana', 'uva'}
# Ou
frutas = ['maçã', 'banana', 'uva']
frutas = set(frutas)

# Criando um conjunto vazio
vazio = set()

# Removendo duplicatas
numeros = [1, 2, 2, 3, 4, 4, 4]
unicos = set(numeros)
print(unicos)

# Sets não posssuem ordem garantida
cores = {'azul', 'verde', 'vermelho'}
# Ao exibir, os elementos podem ser escritos em uma ordem diferente, porque sets não possuem índice 
print(cores)

# Adicionando elementos
nomes = {'Ana', 'Carlos'}
nomes.add('João')

# Removendo elementos
nomes.remove('Carlos')
# Ou
nomes.discard('Caio')

# Fazendo operações entre sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# União
c = a | b
print(c)

# Interseção
d = a & b
print(d)

# Diferença
e = a - b
print(e)

# Elementos exclusivos de cada conjunto
f = a ^ b
print(f)

# Ex 1:
s = {1, 2, 2, 3}
print(s)

# Ex 2:
A = {1, 2, 3}
B = {3, 4}
print(A & B)

# Ex 3:
nomes = ['Ana', 'Carlos', 'Ana', 'João', 'Carlos']
nomes = set(nomes)
for nome in nomes:
    print(nome)

# Ex 4:
A = {1, 2, 3}
B = {3, 4}
print(A | B)
print(A - B)

# Desafio:
turma_a = {'Ana', 'Carlos', 'João', 'Maria'}
turma_b = {'Carlos', 'Pedro', 'Maria', 'Júlia'}
print(turma_a & turma_b)
print(turma_a - turma_b)
print(turma_b - turma_a)
print(turma_a | turma_b)