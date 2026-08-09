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

# Exibindo pelo índice mais abrangente (primeiro)
print(paises['América'])
print(paises['Europa'])

# Exibindo pelo índice específico (segundo) - deve usar ':' para indicar que está incluindo todos os índices mais abrangentes no filtro
print(paises[:,'AR'])

# Exibindo pelos dois índices
print(paises['Europa', 'UK'])

# Criando novas Series a partir da série com indexação hierárquica
paises_europa = paises['Europa']
paises_america = paises['América']
