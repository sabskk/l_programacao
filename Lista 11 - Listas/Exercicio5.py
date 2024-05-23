# Faça um Programa Python que leia uma lista de 10 números inteiros e mostre-os na ordem inversa.

lista=[]
i = 0

while i <= 9:
    i += 1
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

lista.reverse()
print("Lista reversa:",lista)