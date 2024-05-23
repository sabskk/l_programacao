#Faca um algoritmo que receba como entrada os dados de um funcionário: nome, cargo e salário. Calcule um
#aumento de 5% sobre o salário. Ao final mostrar o novo salário calculado:

nome = input("Digite seu nome:")
cargo = input("Digite seu cargo:")
salario = float(input("Digite seu salário:"))
aumento = ((salario/100)*5) + salario

print("Seu salário é de ",aumento)