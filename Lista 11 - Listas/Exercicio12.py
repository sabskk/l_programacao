# Faça um Programa Python que leia uma lista com 10 números inteiros, calcule e mostre o maior e menor elemento da
# lista.

numeros = []

for contador in range(0,5):
    valor = input("Insira um número:")
    numeros.append(valor)

print("Lista de números digitados:",numeros)
print("Maior valor da lista:",max(numeros))
print("Menor valor da lista:",min(numeros))