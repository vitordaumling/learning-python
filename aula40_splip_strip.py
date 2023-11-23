"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') # divide a frase na virgula

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas) # frase splitada
print(lista_frases) # frase unida na lista
frases_unidas = ', '.join(lista_frases) # une a frase pela vigula (uma unica string)
print(frases_unidas)