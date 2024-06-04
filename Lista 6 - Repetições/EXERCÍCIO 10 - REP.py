#EXERCÍCIO 10 - LISTA 06 (REPETIÇÃO)
while True:
    print("**********************************")
    print("Operações da Calculadora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do Programa")
    Opcao = int(input("Escolha a opção desejada:"))
    if (Opcao == 5):
        print("Fim do programa.....")
        break
    Valor1 = int(input("Digite o primeiro valor:"))
    Valor2 = int(input("Digite o segundo valor:"))
    print("**********************************")
    if (Opcao == 1):
        Resultado = Valor1 + Valor2
        print("Resultado:",Valor1," + ",Valor2," = ",Resultado)
    if (Opcao == 2):
        Resultado = Valor1 - Valor2
        print("Resultado:",Valor1," - ",Valor2," = ",Resultado)
    if (Opcao == 3):
        Resultado = Valor1 * Valor2
        print("Resultado:",Valor1," * ",Valor2," = ",Resultado)
    if (Opcao == 4):
        Resultado = Valor1 / Valor2
        print("Resultado:",Valor1," / ",Valor2," = ",Resultado)