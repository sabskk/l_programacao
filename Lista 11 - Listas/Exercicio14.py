# Desenvolva um script em linguagem Python que peça as quatro notas de 10 alunos, calcule e armazene num vetor a 
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.

medias = []
total = 0
i = 0

while i <=4:
    print("--- NOTAS DO ALUNO ---")
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: ")) 
    nota3 = float(input("Digite sua terceira nota: "))
    nota4 = float(input("Digite sua quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4)/2
    print("Média do aluno: ",media)
    medias.append(media)

    if (media >= 7):
        total += 1

print("Médias digitadas: ",medias)
print("Total de alunos aprovados: ",total)