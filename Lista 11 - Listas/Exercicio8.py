# Faça um Programa Python que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista
# PAR e os números impares na lista IMPAR. Imprima ao final os três vetores.

numeros = []
pares = []
impares = []

for contador in range(0,5):
    valor = int(input("Digite um número inteiro:"))
    numeros.append(valor)

    if (valor % 2) == 0 :
        pares.append(valor)
    else:
        impares.append(valor)

print("Lista de números digitados:",numeros)
print("Lista de números pares:",len(pares))
print("Lista de números impares:",len(impares))