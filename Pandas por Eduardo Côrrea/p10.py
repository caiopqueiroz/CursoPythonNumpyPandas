# Indexação hierárquica
import pandas as pd


# Criando uma Series com índices hierárquicos
paises = pd.Series(
    ['Peso', 'Real', 'Euro', 'Euro', 'Libra'],
    index = [
        ['América', 'América', 'Europa', 'Europa', 'Europa'],
        ['AR', 'BR', 'FR', 'IT', 'UK']
    ]
)
print(paises)