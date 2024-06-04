# Desenvolva um script em linguagem Python, utilizando Dicionários, que solicite ao usuário inserir o nome de 10
# amigos e seus telefones e os mostre na tela.

dicionario = {}

for range in range(0, 10):
    nome = input("Digite o nome de seu amigo: ")
    tele = float(input("Digite o telefone de seu amigo: "))
    dicionario[nome] = tele

print(dicionario)