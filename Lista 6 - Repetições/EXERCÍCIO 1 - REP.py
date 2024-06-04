#EXERCÍCIO 01 - LISTA 06 (REPETIÇÃO)
#FOR
Numero = int(input("Digite um número para a tabuada desejada:"))
for Contador in range(1,11):
    Resultado = Numero * Contador
    print(Numero," X ",Contador," = ",Resultado)

#WHILE
Contador = 1
Numero = int(input("Digite um número para a tabuada desejada:"))
while (Contador <=10):
    Resultado = Numero * Contador
    print(Numero," X ",Contador," = ",Resultado)
    Contador = Contador + 1