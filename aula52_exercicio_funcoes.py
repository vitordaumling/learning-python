# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4

def multiplicar(numero, multiplicador):
    try:
        numero = int(numero)
        multiplicador = int(multiplicador)
        
        return numero * multiplicador
    except:
        return "Algum digito informado não é um número!"
    
    
print(multiplicar(2, 8))