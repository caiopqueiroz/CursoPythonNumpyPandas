# Calculando estatísticas básicas - média, mediana e moda
import pandas as pd 
import numpy as np


# Criando um df
dados = {
    'jogador': ['Marcelo', 'Pedro', 'Marcelo', 'Adriano', 'Mauro', 'Pedro', 'Marcelo'],
    'infracao': [
        'FALTA VIOLENTA',
        'RECLAMAÇÃO',
        'FALTA COMUM',
        'RECLAMAÇÃO',
        'FALTA COMUM', 
        'FALTA VIOLENTA',
        'RECLAMAÇÃO'
    ],
    'punicao': [4, 1, 3, 2, 4, 4, 2],
    'punicao_alternativa': [2, 1, 4, 1, 1, 5, 6]
}
df = pd.DataFrame(dados)

# Calculando a média dos dias de punição 
print(df['punicao'].mean())
# ou 
print(np.mean(df['punicao']))

# Mediana
print(df['punicao'].median())

# Moda
print(df['punicao'].mode())

# Exibindo estatística numéricas diversas 
print(df['punicao'].describe())

# Levando em consideração 2 punições diferentes, é possível calcular diferença de amplitude entre elas 
print(df['punicao_alternativa'].max() - df['punicao_alternativa'].min()) # 5
print(df['punicao'].max() - df['punicao'].min()) # 3

# Variância 
print(df['punicao_alternativa'].var()) # 4.47
print(df['punicao'].var()) # 1.47

# Desvio padrão 
print(df['punicao_alternativa'].std()) # 2.11
print(df['punicao'].std()) # 1.21
# Isso significa que, a punição alternativa apresenta maior variablidade, se afasta mais de 2 jogos da média