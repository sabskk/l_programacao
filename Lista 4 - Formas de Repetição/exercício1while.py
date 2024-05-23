# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 à 10. O usuário
# deve informar de qual número ele deseja ver a tabuada.

contador = 1
numero = int(input("Digite a tabuada escolhida: "))
while (contador<=10):
    resultado = numero * contador
    print (numero,"x",contador,"=",resultado)
    contador+=1