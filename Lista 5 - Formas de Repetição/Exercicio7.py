# Construir um algoritmo que leia o nome e idade de 200 atletas. Após verificar o total de atletas em cada
# categoria:
# Idade de 13 a 17 anos – Categoria de Base
# Idade de 18 a 40 anos – Categoria Profissional
# Idade acima 40 anos – Categoria Veterano

totalB = 0
totalP = 0
totalV = 0

for contador in range(10):
    nome = input("Digite seu nome: ").title()
    salario = float(input("Digite seu salário: R$"))
    if salario < 18:
        totalB += 1
    if salario >= 18 and salario <= 40:
        totalP += 1   
    if salario > 40:
        totalV += 1
    
print("Total de pessoas com a categoria Base: ",totalB)
print("Total de pessoas com a categoria Profissional: ",totalP)
print("Total de pessoas com a categoria Veterano: ",totalV)