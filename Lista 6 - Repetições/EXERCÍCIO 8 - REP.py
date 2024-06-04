#EXERCÍCIO 08 - LISTA 06 (REPETIÇÃO)
for Contador in range(10):
        Numero = int(input("Digite um número inteiro positivo:"))
        if Numero < 0:
                print("Número negativo encerra o programa!")
                break
        if (Numero % 2) == 0:
                print("O número digitado é par.")
        else:
                print("O número digitado é ímpar.")