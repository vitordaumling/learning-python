""" Calculadora com while """
while True :
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite o operador (+-/*): ')
    num_1_float = 0
    num_2_float = 0
    
    numeros_validos = None
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    operadores_permitidos = '+-*/'
    
    if numeros_validos == None:
        print('Um ou ambos os números digitados são inválidos!')
        continue
    
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    print('Realizando o cálculo, confira o resultado abaixo:')
    resultado = 0
    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'{num_1_float} + {num_2_float} = {resultado}' )
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'{num_1_float} - {num_2_float} = {resultado}' )
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(f'{num_1_float} * {num_2_float} = {resultado}' )
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(f'{num_1_float} / {num_2_float} = {resultado}' )
    
    #####
    sair = input('Quer sair? [s] Sim: ').lower().startswith('s')
    print(sair)
    if sair is True:
        break
    
