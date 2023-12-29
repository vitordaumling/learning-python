# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    # Se digitar repetido, só salva 1 unico valor
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)