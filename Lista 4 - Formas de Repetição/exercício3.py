#Escreva um programa que leia 10 valores inteiros e encontre o maior e o menor deles.

contador = 1
maior = 0
menor = 999999
while (contador <= 10):
    numero = int(input("Digite um valor:"))
    if (numero > maior):
        maior = numero
    if (numero < menor):
        menor = numero
    contador+=1
print ("Maior número lido: ",maior)
print ("Menor número lido: ",menor)