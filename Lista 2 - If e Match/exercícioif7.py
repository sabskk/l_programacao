#Escrever um algoritmo para ler nome e idade de um atleta e verificar a categoria:
#Idade			Categoria
#0..10			 Infantil
#11..17			 Juvenil
#18..30 		 Adulto
#30..60			 Sênior

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

if idade>=10:
    print("Infantil.")
if idade<=11 and idade>=17:
    print ("Juvenil.")
if idade<=18 and idade>=30:
    print ("Adulto.")
if idade<=30 and idade>=60:
    print ("Sênior.")