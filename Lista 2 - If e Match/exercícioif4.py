#Escrever um algoritmo para ler o nome de um aluno e a media final. Após verificar:
#Média < 5            – Aluno Reprovado
#Média entre 5 e 7  – Aluno em Recuperação
#Média >= 7          – Aluno Aprovado

nome = input("Digite seu nome:")
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
n3 = float(input("Digite sua terceira nota:"))
media = (n1+n2+n3)/3

if media<5:
    print("Aluno reprovado.")
if media>5 and media<7:
    print("Aluno em recuperação.")
if media<7:
    print("Aluno aprovado.")