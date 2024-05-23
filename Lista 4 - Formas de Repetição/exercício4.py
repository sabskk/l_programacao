# Escreva um programa que lido um número, calcule e informe o seu fatorial. 
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.

fatorial = 1
numero = int(input("Digite um número: "))
for contador in range (1, numero+1):
    fatorial = fatorial * contador
print ("Fatorial o número", numero,": ",fatorial)