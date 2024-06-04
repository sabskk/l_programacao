#EXERCÍCIO 05 - LISTA 06 (REPETIÇÃO)
Soma = 0
Quantidade = 0
Maior = 0
Menor = 9999
while True:
    Numero = int(input("Digite um número inteiro:"))
    if Numero < 0:
        break
    Soma = Soma + Numero
    Quantidade = Quantidade + 1
    if Numero > Maior:
        Maior = Numero
    if Numero < Menor:
        Menor = Numero
print("Quantidade de números digitados:",Quantidade)
print("Soma dos números:",Soma)
Media = Soma / Quantidade
print("Média dos números:",Media)
print("Maior número digitado",Maior)
print("Menor núemro digitado:",Menor)