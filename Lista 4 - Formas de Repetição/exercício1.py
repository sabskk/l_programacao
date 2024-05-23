# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 à 10. O usuário
# deve informar de qual número ele deseja ver a tabuada.

numero = int(input("Digite a tabuada esolhida: "))
for contador in range (1, 11):
    resultado = numero * contador
    print (numero,"x",contador,"=",resultado)