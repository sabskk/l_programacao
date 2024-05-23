# Faça um Programa Python que leia uma lista de 5 números inteiros e mostre-os no final

lista=[]

for contador in range(5):
    numero=input("Digite um número:")
    lista.append(numero)
    
print("Numeros",lista)
