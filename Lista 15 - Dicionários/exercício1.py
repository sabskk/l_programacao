# Desenvolva um código em Python que adicione em um dicionário “D” os seguintes campos: nome, idade e mostre os dados
# no final.

dicionario = {}

n = int(input("Digite quantos elementos deseja cadastrar: "))

for contador in range(0,n):
    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    dicionario[nome] = idade

print (dicionario)