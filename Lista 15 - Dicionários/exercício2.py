# Elabore um script em  linguagem Python, utilizando Dicionários, que contenha 4 funcionários, com o índice numérico e
# seu nome. Em seguida, solicite do usuário demitir um dos funcionários conforme o número de cadastro e mostre na tela
# os funcionários restantes.

dicionario = {}

for range in range(0, 4):
    nome = input("Digite o nome do funcionário: ")
    cod = input("Digite o código do funcionário: ")
    dicionario[nome] = cod

print(dicionario)

delete = input("Qual o fucionário que deseja demitir: ")
del dicionario[delete]
print(dicionario)