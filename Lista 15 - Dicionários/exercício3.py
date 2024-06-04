# Desenvolva um script em linguagem Python, utilizando Dicionários, que solicite ao usuário inserir o nome de 05
# produtos de papelaria e seus respectivos preços e os mostre na tela.

dicionario = {}

for range in range(0, 5):
    nome = input("Digite o nome do item: ")
    preco = float(input("Digite o preço do item: "))
    dicionario[nome] = preco

print(dicionario)