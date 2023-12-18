# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4

# def multiplicar(numero, multiplicador):
#     try:
#         numero = int(numero)
#         multiplicador = int(multiplicador)
        
#         return numero * multiplicador
#     except:
#         return "Algum digito informado não é um número!"

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        try:
            return numero * multiplicador
        except:
            return "Algum digito informado não é um número!"
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2), triplicar(2), quadruplicar(2))