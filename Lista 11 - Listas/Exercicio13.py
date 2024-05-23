# Elabore um script em linguagem Python que leia de 10 números reais, inserindo-os numa lista e ao final, mostre-os
# na ordem inversa.

numeros = []

for contador in range(0,5):
    valor = input("Insira um número:")
    numeros.append(valor)

numeros.reverse()
print("Lista invertida:",numeros)