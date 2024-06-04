#EXERCÍCIO 04 - LISTA 06 (REPETIÇÃO)
Fatorial = 1
Numero = int(input("Digite um número para ser fatorado:"))
for Contador in range(1,Numero+1):
    Fatorial = Fatorial * Contador
print("Fatorial do número",Numero," = ",Fatorial)