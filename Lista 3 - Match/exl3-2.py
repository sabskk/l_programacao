#Faça um programa que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Informar
#também o percentual de juros do mês.

deposito = float(input("Digie o valor do seu depósito:"))
juros = float(input("Digite o valor dos juros aplicados:"))
valor = deposito(deposito*juros /100)
print("O valor do rendimento é de: R$", valor)