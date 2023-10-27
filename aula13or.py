# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
print(not True)  # False
print(not False)  # True

senha_permitida = '123456'



if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
   print('Entrar')
else:
    print('Sair')

## exemplos usando not
# Comparação
if not senha_digitada:
    print('senha não digitada!')
elif senha_digitada != senha_permitida:
    print('Senha Incorreta!')
    

# Avaliação de curto circuito
# senha = input('Senha: ') or 'Sem senha'
# print(senha)