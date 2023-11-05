""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    ## se tiver break o else não é executado!
    print('Não encontrei um espaço na string.')
print('Fora do while.')