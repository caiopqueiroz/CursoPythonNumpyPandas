# Ordenando data frames por uma coluna
import pandas as pd 


dados = {
    'nadador': ['Simonas Bilis', 'Benjamin Proud', 'Anthony Ervin', 'Florent Manaudou', 'Andriy Hovorov', 'Nathan Adrian', 'Bruno Fratus', 'Brad Tandy'],
    'nacionalidade': ['Lituânia', 'Grâ-Bretanha', 'Estados Unidos', 'França', 'Ucrânia', 'Estados Unidos', 'Brasil', 'África do Sul'],
    'tempo': [22.08, 21.68, 21.40, 21.41, 21.74, 21.49, 21.79, 21.79]
}
raia = [1, 2, 3, 4, 5, 6, 7, 8]
df = pd.DataFrame(
    dados,
    index = raia
)

# Atribuindo um rótulo à coluna de índices 
df.index.name = 'raia'

# Usando a função sort_values() para ordenar o df de acordo com a coluna tempo, assim exibindo os nadadores na ordem do pódio
print(df.sort_values(
    'tempo'
))

# Exibindo apenas o campeão usando a função nsmallest()
print(df.nsmallest(
    1,
    'tempo'
))

# Mostrando apenas o pódio usando as funções head() para exibir os 3 primeiros e sort_values() para ordená-los pelo menor tempo 
print(
    df.sort_values('tempo').head(3)
)

# Da mesma forma, exibindo os 3 últimos colocados com tail()
print(
    df.sort_values('tempo').tail(3)
)

# Calculando e exibindo a média de tempo gasto pelos nadadores usando mean()
print(df['tempo'].mean())

# Exibindo, ordenados, apenas os nadadores que fizeram tempos menores que a média 
print(
    df[df['tempo'] < df['tempo'].mean()].sort_values('tempo') 
)

# Agora, os nadadores com tempos maiores que a média 
print(
    df[df['tempo'] > df['tempo'].mean()].sort_values('tempo')
)

# Usando a função rank() com o parâmetro method = 'min' para que nadadores com tempos iguais recebem a mesma classificação (próximo número mínimo disponível) - nessa visualização, a identificação de cada nadador é feita pela coluna index, que é a raia
print(df['tempo'].rank(method = 'min').sort_values())
