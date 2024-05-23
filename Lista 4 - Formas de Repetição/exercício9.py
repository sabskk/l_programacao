# Faça um programa que peça nome e nota do aluno (entre zero e dez). Mostre uma mensagem caso o valor nota
# seja inválido e continue pedindo até que o usuário informe um valor válido.

nome = input("Digite seu nome: ")
while True:
    nota = float(input("Digite sua nota, de 0 a 10: "))
    if nota < 0 or nota > 10:
        print ("Valor inválido, tente novamente.")
        continue
    else: 
        print ("Nome do aluno: ",nome)
        print ("Nota do aluno: ",nota)