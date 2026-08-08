 # O valor NaN
import pandas as pd


verde = pd.Series(
    [1, 0, 1, 0],
    index = ['BR', 'FR', 'IT', 'UK']
    )
azul = pd.Series(
    {'AR': 1, 'BR': 1, 'FR': 1, 'IT': 1, 'UK': 0}
)

print('Soma:')
print(verde + azul)

# Exibindo apenas países que possuem verde e azul na bandeira
soma = verde + azul
print(soma.index[
    soma == 2
])

# Mostrando que, ao somar verde + azul, a Argentina aparece como NaN pois não existe na primeira Series, assim, a soma NaN + 1 = NaN
print(soma.isnull())


