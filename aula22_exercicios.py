"""
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input("Informe a hora em números inteiros: ")

try:
    hora_int = int(entrada)
    
    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia!")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde!")
    elif hora_int >=18 and hora_int <=23:
        print("Boa noite!")
    else:
        print("Não conheço essa hora!")
    
except:
    print('Por favor digite apenas números inteiros!')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""
nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto!")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal!")
    else:
        print("Seu nome é muito grande!")
else:
    print('Digite mais de uma letra.') 
