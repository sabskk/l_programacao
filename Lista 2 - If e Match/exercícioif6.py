#Escrever um algoritmo para ler nome e a sigla do estado civil de uma pessoa e verificar a classificação:
#Sigla			Classificação
#S				Solteiro 
#C				Casado 	
#V				Viúvo 
#D				Divorciado

nome = input("Digite seu nome:" )
print("Estado civil: S - Solteiro")
print("              C - Casado")
print("              V - Viúvo")
print("              D - Divorciado")
estc = input("Escolha seu estado civil:")

if estc=="S":
    print("Nome:", nome)
    print("Seu curso é soleiro.")
if estc=="C":
    print("Nome:", nome)
    print("Seu curso é casado.")
if estc=="V":
    print("Nome:", nome)
    print("Você é viúvo.")
if estc=="D":
    print("Nome:", nome)
    print("Você é divorciado.")