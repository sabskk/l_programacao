#Escrever um algoritmo para ler um numero de 1 a 7 correspondente ao dia da semana e exibir o dia correspon-
#dente na tela: 
#Exemplo: 1 – Segunda-feira,  2 – Terça-feira
#OBS: Mostrar mensagem se valor digitado é inválido.

dia = int(input("Digite um valor de 1 - 7:"))

match dia:
    case "1":
        print("1 = Domingo")
    case "2":
        print("2 = Segunda-feira")
    case "3":
        print("3 = Terça-feira")
    case "4":
        print("4 = Quarta-feira")
    case "5":
        print("5 = Quinta-feira")
    case "6":
        print("6 = Sexta-feira")
    case "7":
        print("7 = Sábado")
    case "_":
        print("Dia da semana inválido.")