"""
Repetições com contador
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 13:
        print('não vou mostrar o 13!')
        continue
    
    print(contador)
    
    ## parar o contador com 'break'
    if contador == 27:
        break
    

print('Acabou')
