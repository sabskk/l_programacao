# Para construir o programa a seguir, considere que os usuários só informarão números inteiros. Crie um
# programa que receba 10 números digitados e exiba todos os números pares e ímpares.

for i in range (10):
    numero  = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print ("Número negativo. Fim do programa.")
        break
    if (numero % 2) == 0:
        print ("O número", numero, "é um número par.")
    else:
        print ("O número", numero, "é um número ímpar.")