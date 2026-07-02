# Criando um dicionário
aluno = {
    'nome': 'Caio',
    'idade': 20,
    'nota': 9.8
}

# Alterando um valor 
aluno['idade'] = 19

# Adicionando novo valor 
aluno['cidade'] = 'Pará de Minas'

# Removendo um valor (valores são removidos usando suas chaves)
del aluno['nota']
# Utilizando a função pop(), o valor removido pode ser armazenado em outra variável
cidade = aluno.pop('cidade')

# Exibindo um dicionário (apenas suas chaves)
for chave in aluno:
    print(chave)

# Apenas os valores
for valor in aluno.values():
    print(valor)

# Chaves e valores
for chave, valor in aluno.items():
    print(chave, valor)

# Verificar se existe uma chave
if 'idade' in aluno:
    pass

# Obter valor (caso não exista a chave 'nome', nesse caso será atribuído à variável o valor 0)
nome = aluno.get('nota', 0)

# Exemplo de banco de dados + visualização
dados = {
    'Nome': ['Ana', 'Carlos', 'João'],
    'Idade': [20, 25, 30]
}
for chave, valor in dados.items():
    print(chave, end=' | ')
    for elemento in valor:
        print(elemento, end='   ')
    print()

# Ex 1:
pessoa = {
    'nome': 'Ana',
    'idade': 18
}
print(pessoa['nome'])

# Ex 2:
d = {
    'x': 10
}
d['x'] = 20
print(d)

# Ex 3:
aluno = {
    'nome': 'Caio',
    'idade': 19,
    'altura': 175
}
peso = aluno.get('peso', 0)
print(peso)

# Ex 4:
d = {
    'a': 1,
    'b': 2
}
for chave, valor in d.items():
    print(chave, valor)

# Desafio:
notas = {
    'Ana': 9,
    'Carlos': 7,
    'João': 10,
    'Maria': 8
}
maiores_notas = [chave for chave, valor in notas.items() if valor >= 9]
print(maiores_notas)