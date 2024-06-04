# Faça um programa, utilizando Dicionário, que peça para o usuário inserir o nome  de 05 amigos e seus respectivos
#telefones.  Após, peça ao usuário para inserir um novo nome e telefone.

dicionario = {}

for range in range(0, 5):
    nome = input("Digite o nome de seu amigo: ")
    tele = float(input("Digite o telefone de seu amigo: "))
    dicionario[nome] = tele

print(dicionario)

nome2 = input("Insira um novo nome: ")
tele2 = float(input("Digite um novo telefone: "))
dicionario[nome2] = tele2

print(dicionario)