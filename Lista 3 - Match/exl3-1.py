#Elaborar um programa que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar
#(US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis
#com o usuário.

cot = float(input("Qual a cotação atual do dólar:"))
valor = float(input("Informe um valor:"))
print("Conversão de valores para:")
print("D - Dólar")
print("R - Real")
con = input("Escolha sua conversão:")
real = (valor * cot)
dol = (valor/cot)

match con:
    case "D":
        print("Seu valor é de:", real)
    case "R":
        print("Seu valor é de:", dol)