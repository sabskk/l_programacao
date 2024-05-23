#Escrever um algoritmo para ler o nome de um aluno e a sigla do curso e verificar:
#Sigla			Curso
#ADM 		    Administração
#DIR			Direito
#CEX			Comércio Exterior

nome = input("Digite seu nome:" )
print("Cursos: ADM - Adminisração")
print("        DIR - Direito")
print("        CEX - Comércio Exterior")
curso = input("Escolha a sigla do seu curso:")

if curso=="ADM":
    print("Nome:", nome)
    print("Seu curso é Administração.")
if curso=="DIR":
    print("Nome:", nome)
    print("Seu curso é Direito.")
if curso=="CEX":
    print("Nome:", nome)
    print("Seu curso é Comércio Exterior.")