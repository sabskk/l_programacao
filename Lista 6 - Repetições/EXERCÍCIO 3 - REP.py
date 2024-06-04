#EXERCÍCIO 03 - LISTA 06 (REPETIÇÃO)
Contador = 1
Maior = 0
Menor = 999
for Contador in range(1,11):
    Numero = int(input("Digite um número:"))
    if (Numero > Maior):
        Maior = Numero
    if (Numero < Menor):
        Menor = Numero
    Contador = Contador+1
print("Maior número lido:",Maior)
print("Menor número lido:",Menor)