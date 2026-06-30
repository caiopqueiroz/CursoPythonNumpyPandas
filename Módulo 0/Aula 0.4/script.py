# Modelo de list comprehension
quadrados = [numero ** 2 for numero in range(5)]
print(quadrados)

# Estrutura geral:
#[expressao for elemento in iteravel]

# Exemplo:
dobros = [x * 2 for x in range(5)]
# Leitura: para cada x no range(5), coloque x * 2 na nova lista 

# Exemplo colocando novos valores utilizando o for (if/else -> no início)
numeros = [f'{numero} é par' if numero % 2 == 0 else f'{numero} é ímpar' for numero in range(1, 11)]

# Exemplo filtrando valores (if somente -> no fim)
pares = [numero for numero in range(1, 11) if numero % 2 == 0]

precos = [10, 20, 30]
descontos = [preco * 0.9 for preco in precos]

# Ex 1:
resultado = [x + 10 for x in range(8)]
print(resultado)

# Ex 2:
impares = [x for x in range(7) if x % 2 == 1]
print(impares)

# Ex 3:
quadrados = [numero ** 2 for numero in range(10) if numero % 2 == 0]
print(quadrados)

# Ex 4:
posicao = ['Positivo' if x > 0 else 'Zero ou negativo' for x in [-2, 3, 0, 5]]
print(posicao)

# Desafio:
caixa_alta = [nome.upper() for nome in ['Ana', 'Carlos', 'João', 'Beatriz']]
print(caixa_alta)
nomes_grandes = [nome for nome in ['Ana', 'Carlos', 'João', 'Beatriz'] if len(nome) > 5]
print(nomes_grandes)