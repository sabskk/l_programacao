#EXERCÍCIO 06 - LISTA 06 (REPETIÇÃO)
Numero = int(input("Digite um número inteiro:"))
Contador = 0
Divisor = 0
while Divisor <= Numero or Contador < 2:
    Divisor = Divisor + 1
    RestoDivisao = Numero % Divisor
    if RestoDivisao == 0:
        Contador = Contador + 1
if Contador <= 2:
        print("Número digitado",Numero,"é primo.")
else:
        print("Número digitado:",Numero,"não é primo.")