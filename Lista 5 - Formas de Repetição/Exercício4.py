# Faça um algoritmo que receba como entrada os dados de 300 funcionários de uma empresa: nome, cargo.
# Após verifique a quantidade de funcionários de cada cargo:
# Engenheiro Mecânico
# Engenheiro Elétrico
# Engenheiro Civil

totalM = 0
totalE = 0
totalC = 0

for contador in range(10):
    nome = input("Digite seu nome: ")
    print = ("Cargos:")
    print = ("M = Engenheiro Mecânico / E = Engenheiro Elétrico / C = Engenheiro Civil")
    curso = input("Digite seu cargo: ").upper()
    if curso == "M":
        totalM += 1
    if curso == "F":
        totalE += 1   
    if curso == "M":
        totalC += 1
    
print("Total de profissionais em Engenharia Mecânica: ",totalM)
print("Total de profissionais em Engenharia Elétrica: ",totalE)
print("Total de profissionais em Engenharia Civil: ",totalC)