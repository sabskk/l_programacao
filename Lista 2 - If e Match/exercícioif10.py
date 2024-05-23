#Escrever um algoritmo para ler dois valores e escolher a operação matemática desejada (adição, subtração,
#multiplicação e divisão). Ao final exibir o resultado.
#Exemplo:  valor1 =  2
#		   valor2 =  3
#          operação = adição
#          Resultado = 5


print("Operações: T - Técnico")
print("        + - Soma")
print("        - - Subração")
print("        / - Divisão")
print("        * - Muliplicação")
op = input("Informe sua operação escolhida:")
v1 = float(input("Informe seu primeiro valor:"))
v2 = float(input("Informe seu segundo valor:"))
soma = v1+v2
sub = v1-v2
div = v1/v2
mul = v1*v2

match op:
    case "+":
        print("R =", soma)
    case "-":
        print("R =", sub)
    case "/":
        print("R =", div)
    case "*":
        print("R =", mul)