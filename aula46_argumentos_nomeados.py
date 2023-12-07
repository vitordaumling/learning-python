"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# argumentos posicionais
soma(1, 2, 3)
# argumentos nomeados - nomeando todos, não vai importar a ordem
soma(z=3, x=5, y=9)

# aqui a partir do momento que nomeio, todos os args que vem depois precisam ser nomeados também
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')