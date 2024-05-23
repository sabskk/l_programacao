# Faça um Programa Python que leia uma lista de 5 números inteiros, mostre a soma dos elementos da lista.

lista=[]
i = 0

while i <= 4:
    i += 1
    numeros=int(input("Digite um número inteiro:"))
    lista.append(numeros)
    soma=sum(lista)

print("total somatoria:",soma)