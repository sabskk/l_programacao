# Escrever um programa que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos.

contador = 1
soma = 0
while (contador <= 10):
    numero = int(input("Digite um valor:"))
    soma+=numero
    contador+=1
print ("Soma dos números lidos: ",soma)