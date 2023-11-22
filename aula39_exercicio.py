"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os


lista = []

while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")
    
    if opcao == "i":
        os.system('clsi')
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == "a":
        indice_str = input("Selecione o indice para apagar: ")
        
        try:
            indice = int(indice_str)
            del lista[indice]
            print("Registro deletado com sucesso!")
        except ValueError:
            print("O valor não é um número!")
        except IndexError:
            print("O índice que voce digitou não existe")
        except Exception:
            print("Erro desconhecido!")
        
    elif opcao == "l":
         os.system('cls')
         
         if len(lista) == 0:
             print("Nada para listar!")
        
        
         for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == "s":
        break
        
    else:
        print("Por favor! Escolha i, a, l ou s!")