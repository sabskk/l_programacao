#EXERCÍCIO 09 - LISTA 06 (REPETIÇÃO)
Contador = 1
Nome = input("Digite o nome do aluno:")
Nota = float(input("Digite a nota do aluno (0 à 10):"))
while (Nota > 10) or (Nota < 0):
    print("Nota inválida... Digite um valor entre 0 e 10.")
    Nota = float(input("Digite a nota do aluno:"))