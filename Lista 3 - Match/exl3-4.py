#Escrever um algoritmo para ler nome, salario e o departamento de um funcionário da empresa e após calcular
#seu novo salário, de acordo com o % aumento:

#Sigla			Setor			Aumento %
#V				Vendas 			10%
#C				Compras		    8% 	
#P				Produção        15% 

nome = input("Digite seu nome:")
print("Departamentos: V - Vendas")
print("               C - Compras")
print("               P - Produção")
dep = input("Digite seu departamento:")
sal = float(input("Digite seu salário:"))
V = sal + (sal*0.10)
C = sal + (sal*0.8)
P = sal + (sal*0.15)

match dep:
    case "V":
        print("Seu novo salário é de: R$", V)
    case "C":
        print("Seu novo salário é de: R$", C)
    case "P":
        print("Seu novo salário é de: R$", P)