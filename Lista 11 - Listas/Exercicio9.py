# Faça um Programa Python que peça as duas notas de 10 alunos e armazene numa lista. Calcule e mostre a média de
#cada aluno.

lista=[]
i = 0

while i <= 4:
    i += 1
    print("--- NOTAS DO ALUNO N.",i,"---")
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    media = (nota1 + nota2)/2
    lista.append(media)

print("Média dos alunos, respectivamente:",lista)