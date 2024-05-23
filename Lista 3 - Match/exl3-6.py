#Escrever um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele
#no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o
#seu nome, o salário fixo e salário no final do mês.

nome = input("Digite seu nome:")
salariofixo = float(input("Digite seu salário fixo:"))
vendas = int(input("Digite seu total de vendas: R$"))

comissao = vendas*0.15
salariof = salariofixo+comissao

print("Nome do funcionário:", nome)
print("Salário fixo: R$", salariofixo)
print("Comissão: R$")
print("Salário final: R$", salariof)