# Elabore um programa que leia um número inteiro e indique se o número é primo ou não. Lembrando que os números
# primos são divisíveis somente por 1 e por ele mesmo. No entanto, o número 1 não é primo.

numero = int(input("Digite um número inteiro: "))
cont= 0
divisor = 0

while divisor <= numero or cont < 2:
    divisor = divisor + 1
    restodivisao = numero % divisor
    if restodivisao == 0:
        cont = cont + 1
    
if cont <= 2:
    print("O número", numero, "é primo.")
else:
    print("O número", numero, "não é primo.")