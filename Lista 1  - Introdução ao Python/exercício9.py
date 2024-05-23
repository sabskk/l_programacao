#Faca um algoritmo que receba como entrada os dados de  um funcionário: nome, numero de horas trabalhadas, 
#valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E ao final
#mostrar seu nome e salário final calculado.

nome = input("Digite seu nome:")
horas = float(input("Digite seu número de horas trabalhadas:"))
valorh = float(input("Digite o valor das horas trabalhadas:"))

salario = horas*valorh
inss = salario*00.2
novosalario = salario-inss

print("Seu novo salário é de:", novosalario)