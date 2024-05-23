#Faca um algoritmo que receba como entrada os dados de um aluno: nome, curso, disciplina, nota1, nota2,
#nota3. Calcule a média do aluno e mostre o resultado:

nome = input("Digite seu nome:")
curso = input("Digite seu curso:")
disciplina = input("Digite seu disciplina:")
nota1 = float(input("Digie sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))
media = (nota1+nota2+nota3)/3

print("Nome do aluno:", nome)
print("Curso:", curso)
print("Disciplina:", disciplina)
print("Sua média é:", media)