"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
## deleta o ultimo indice da lista
del lista[-1]
## Limpa a lista
# lista.clear()
lista.insert(100, 5)
print(lista[4])

## Concatenando ou extendendo uma lista
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
## Concatenando a lista A e a lista B e salvando na variavel 'lista_c
lista_c = lista_a + lista_b
## Concatenando a lista A com a lista B
lista_a.extend(lista_b)
print(lista_a)