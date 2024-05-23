# Faça um algoritmo que leia o nome e média final de 50 alunos de um curso. De acordo com a média do aluno
# verificar: 
# Quantidade de alunos Reprovados
# Quantidade de alunos Aprovados

totalR = 0
totalA = 0

for contador in range(10):
    nome = input("Digite seu nome: ").title()
    media = float(input("Digite sua média: "))
    if media < 7:
        totalR += 1
    if media >= 7:
        totalA += 1
    
print("Total de alunos Reprovados: ",totalR)
print("Total de alunos Aprovados: ",totalA)