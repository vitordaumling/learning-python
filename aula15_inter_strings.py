#Interpolação de strings com '%'
"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Vitor'
preco = 125.60187992

variavel = '%s, O preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %08X' % (1560, 1560))


