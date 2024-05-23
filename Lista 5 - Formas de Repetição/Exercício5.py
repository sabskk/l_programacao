# Construir um algoritmo que receba como entrada os dados de  100 funcionários de uma empresa: nome e
# salário. Após verifique a quantidade de funcionários por faixa salarial: 
# Salário menor que  R$ 1.500,00
# Salário maior que R$ 1.500,00 e menor que R$ 3.000,00
# Salário maior que R$ 3.000,00

total1 = 0
total2 = 0
total3 = 0

for contador in range(10):
    nome = input("Digite seu nome: ").title()
    salario = float(input("Digite seu salário: R$"))
    if salario < 1500:
        total1 += 1
    if salario >= 1500 and salario <= 3000:
        total2 += 1   
    if salario > 3000:
        total3 += 1
    
print("Total de pessoas com o salário menor R$1500: ",total1)
print("Total de pessoas com o salário entre R$1500 e R$3000: ",total2)
print("Total de pessoas com o salário maior que R$3000: ",total3)