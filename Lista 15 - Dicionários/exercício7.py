# Faça um programa, utilizando Dicionário, que peça para o usuário inserir o nome do aluno e suas 03 notas numa lista.
# Calcule a média do aluno e mostre ao final, a situação:
# Média < 5, aluno esta Reprovado
# Média entre 5 e 7, aluno esta em Recuperação
# Média >= 7, aluno está Aprovado.

dicionario = {}
notas = []

nome = input("Digite seu nome: ").capitalize()
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

notas.append(n1)
notas.append(n2)
notas.append(n3)
media = (n1 + n2 + n3)/3

dicionario[nome] = notas
print(dicionario)
print("Sua média foi: ",media)

if media < 5:
    print("Aluno reprovado.")
if media >= 5 and media <=6:
    print("Aluno está em recuperação.")
if media >= 7:
    print("Aluno aprovado.")