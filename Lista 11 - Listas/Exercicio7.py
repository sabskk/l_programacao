# Faça um Programa Python que leia uma lista de 10 caracteres, e diga quantas vogais e consoantes foram lidas.
# Mostre a lista ao final.

caracteres = []

totalV = 0
totalC = 0

i = 0

while i <= 9:
    i += 1
    letra = input("Digite uma letra: ").upper()
    caracteres.append(letra)

    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        totalV += 1
    else:
        totalC += 1

print("Lista de letras digitadas:",caracteres)
print("Total de vogais:",totalV)
print("Total de consoantes:",totalC)