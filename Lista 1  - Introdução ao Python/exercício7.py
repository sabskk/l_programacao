#Faça um algoritmo que receba como entrada os dados de uma pessoa: Nome, idade, peso e altura. Após, calcule
#o seu IMC – Índice de Massa Corporal utilizando a formula: massa = peso / (altura * altura) 
#Ao final, mostrar  nome e o IMC calculado.

nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
peso = float(input("Digite seu peso:"))
altura = float(input("Digite seu altura:"))
imc = peso/(altura*altura)

print("Nome:", nome)
print("Seu IMC é de:", imc)