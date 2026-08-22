# Contando frequências com as funções unique(), value_counts() e groupby()
import pandas as pd 


# Criando uma lista de valores inteiros usando a função range()
id = list(range(1, 7))
dados = {
    'sexo': ['F', 'M', 'F', 'F', 'F', 'M'],
    'bairro': ['Belverde', 'Belverde', 'Savassi', 'Anchieta', None, 'Savassi'],
    'valor': [150, 35, 80, 250, 9.9, 25],
    'cartao': ['Master', 'Visa', 'Visa', 'Amex', 'Elo', 'Master']
}
df = pd.DataFrame(dados)
df.index = id
df.index.name = 'id'

# Usando a função unique() para verificar, dentre os atributos catégoricos, quantos diferentes existem em cada um 
print(df['sexo'].unique()) # Existem 2 sexos diferentes: M e F
print(df['bairro'].unique()) # 3 bairros
print(df['cartao'].unique()) # 4 cartões 

# Usando a função value_counts() para contar as observações diferentes dentre cada um dos atributos - ou seja, mostrar quantas vezes cada um aparece 
print(df['sexo'].value_counts())
print(df['bairro'].value_counts())
print(df['cartao'].value_counts())

# Também possível usar o value_counts() em mais de uma coluna ao mesmo tempo, ou seja, ele só vai reconhecer como iguais, nesse caso, as observações que tiverem o mesmo sexo e o mesmo cartão 
print(df[['sexo', 'cartao']].value_counts()) # Com isso, nota-se que ninguém tem o messmo sexo e o mesmo cartão 

# Se usarmos o value_counts() no df inteiro, poderemos ver se há alguma linha exatamente igual outra - as duplicatas
print(df.value_counts())

# Usando a função groupby() para agrupar as observações por bairros iguais e assim somar a quantidade de clientes pela coluna sexo, por exemplo 
print(
    df.groupby('bairro')['sexo'].count()
)

# Calculando a soma da coluna valor quando o bairro é o mesmo
print(
    df.groupby('bairro')['valor'].sum()
)

# Calculando a média para o mesmo caso 
print(
    df.groupby('bairro')['valor'].mean()
)