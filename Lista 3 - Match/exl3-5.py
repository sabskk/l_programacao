#Faça um programa que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de
#custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

prod = input("Digite o nome do produto:")
preco = float(input("Digite o preço do produto:"))
acr = float(input("Digite o valor do acréscimo:"))

precof = preco + (preco*acr/100)

print("Nome do produto:", prod)
print("Preço a pagar: R$", precof)
