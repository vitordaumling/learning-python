nome = 'Vitor Evandro'
altura = 1.67
peso = 60

imc = peso / (altura ** 2)

## forma só com string normais
# print(nome,'tem', altura, 'de altura')
# print('Pesa', peso, 'quilos e seu IMC é ', imc)

##"f-strings", var:.2f - formata numero com casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Usando format
a = 'AAAAA'
b = 'BBBBB'
c = 1.1

string = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
# usando string.format
formato = string.format(a,b,c)
# parametro nomeado
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)