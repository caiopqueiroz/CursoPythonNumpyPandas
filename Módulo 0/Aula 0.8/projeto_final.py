livros = [
    {'titulo': 'Python', 'paginas': 350},
    {'titulo': 'Cálculo', 'paginas': 800},
    {'titulo': 'Python', 'paginas': 350},
    {'titulo': 'Estatística', 'paginas': 420},
    {'titulo': 'Álgebra', 'paginas': 500}
]


def titulos(lista):
    return [livro['titulo'] for livro in lista] 


def titulos_unicos(lista):
    return set([livro['titulo'] for livro in lista])


def titulos_grandes(lista):
    return [livro for livro in lista if livro['paginas'] > 400]


def maior_paginas(lista):
    return max([livro['paginas'] for livro in lista])


def imprimir_relatorio(lista):
    print(f'Quantidade de livros:\n\n{len(lista)}\n')
    print(f'Maior número de páginas:\n\n{maior_paginas(lista)}\n')
    print(f'Títulos únicos:\n')
    for titulo in titulos_unicos(lista):
        print(titulo)


imprimir_relatorio(livros)