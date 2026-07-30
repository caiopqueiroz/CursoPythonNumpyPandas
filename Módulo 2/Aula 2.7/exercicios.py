import pandas as pd
import numpy as np 


dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro'],
    'Idade': [18, np.nan, 19, 22],
    'Nota': [8.5, 7.2, np.nan, 6.4]
}
df = pd.DataFrame(dados)

# Ex 1:
print(df.isna())
print(df.isnull())
print(df.isna().sum())

# Ex 2:
print(df.dropna())

# Ex 3:
print(df.fillna(0))

# Ex 4:
media = df['Idade'].mean()
#df['Idade'] = df['Idade'].fillna(media)
print(df)

# Desafio:
novo_df = df.copy()
novo_df['Idade'] = novo_df['Idade'].fillna(media)
media_nota = novo_df['Nota'].mean()
novo_df['Nota'] = novo_df['Nota'].fillna(media_nota)
print(np.sum(novo_df.isnull())) # Não há mais valores ausentes