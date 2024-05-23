#Escrever um algoritmo para ler nome e idade de uma pessoa e verificar a classificação:
#Idade			Classificação
#0..3			 escreva (‘Bebê’);
#4..11			 escreva (‘Criança’);
#12..17 		 escreva (‘Adolescente’);
#18..60			 escreva (‘Adulto’);
#61..99			 escreva (‘3ª Idade’);

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

if idade>=3:
    print("Você é um bebê?????????")
if idade<=4 and idade>=11:
    print ("Você é uma criança.")
if idade<=12 and idade>=17:
    print ("Você é um adolescente.")
if idade<=18 and idade>=60:
    print ("Você é um adulto.")
if idade>60:
    print ("3ª idade.")