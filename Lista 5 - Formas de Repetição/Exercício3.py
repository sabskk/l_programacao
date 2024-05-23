# Construir um algoritmo que receba como entrada os dados  de 100 alunos de uma Universidade: nome e curso.
# Após verifique a quantidade de alunos de cada curso:
# Arquitetura
# Farmácia
# Medicina
# Odontologia

totalArq = 0
totalFar = 0
totalMed = 0
totalOdo = 0

for contador in range(10):
    nome = input("Digite seu nome: ")
    print = ("Cursos:")
    print = ("A = Arquitetura / F = Farmácia / M = Medicina / O = Odontologia")
    curso = input("Digite seu curso: ").upper()
    if curso == "A":
        totalArq += 1
    if curso == "F":
        totalFar += 1   
    if curso == "M":
        totalMed += 1
    if curso == "O":
        totalOdo += 1 
    
print("Total de alunos em Arquitetura: ",totalArq)
print("Total de alunos em Farmácia: ",totalFar)
print("Total de alunos em Medicina: ",totalMed)
print("Total de alunos em Odontologia: ",totalOdo)
