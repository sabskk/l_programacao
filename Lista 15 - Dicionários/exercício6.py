# Faça um programa, utilizando Dicionário, que peça para o usuário inserir o nome de 05 produtos de mercado e seus
# respectivos preços e os mostre na tela.

dicionario = {}

for range in range(0, 5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    dicionario[nome] = preco

print(dicionario)