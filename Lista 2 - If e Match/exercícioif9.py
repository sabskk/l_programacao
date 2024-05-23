#Construir um algoritmo para cadastrar os dados de um funcionário, a partir dos dados de entrada: nome, cargo
#e salário. 
#Sigla		Cargo		
#T			Técnico		
#E			Engenheiro de Software
#A			Analista Sistemas
#P			Programador
#W			Web-Designer
#G			Gerente Projetos	

nome = input("Digite seu nome:")
print("Cargos: T - Técnico")
print("        E - Engenheiro de Software")
print("        A - Analista de Sistemas")
print("        P - Programador")
print("        W - Web-Designer")
print("        G - Gerente de Projetos")
cargo = input("Informe seu cargo:")

match cargo:
    case "T":
        print("Seu cargo é Técnico.")
    case "E":
        print("Seu cargo é Engenheiro de Software.")
    case "A":
        print("Seu cargo é Analista de Sistemas.")
    case "P":
        print("Seu cargo é Programador.")
    case "W":
        print("Seu cargo é Web-Designer.")
    case "G":
        print("Seu cargo é Gerente de Projetos.")
    case _:
        print("Você não trabalha nesta empresa.")