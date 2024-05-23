#Escrever um algoritmo para ler nome e a sigla do estado de nascimento de uma pessoa e verificar a
#classificação:
#Sigla			Classificação
#RS				Rio Grande do Sul
#SC				Santa Catarina 
#PR				Paraná

nome = input("Digite seu nome:" )
print("Estados do sul: RS - Solteiro")
print("                SC - Casado")
print("                PR - Viúvo")
estado = input("Escolha seu estado:")

match estado:
    case "RS":
        print("Seu estado é Rio Grande do Sul.")
    case "SC":
        print("Seu estado é Santa Catarina.")
    case "PR":
        print("Seu estado é Paraná.")
    case _:
        print("Você não é do sul.")