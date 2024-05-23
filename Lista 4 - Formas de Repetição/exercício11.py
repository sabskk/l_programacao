# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;       Idade: entre 0 e 100;
# Salário: maior que zero;            Sexo: ‘F' ou ‘M';
# Estado Civil: ‘S', ‘C’, ‘V', ‘D';

while True:
    nome = input("Digite seu nome: ")
    if len(nome) < 3:
        print ("Nome deve ser maior que 3 caracteres, tente novamente.")
    break

while True:
    salário = float(input("Digite seu salário: "))
    if salário < 0:
        print ("Sálario inválido, tente novamente.")
    break

while True:
    print("S - Solteiro")
    print("C - Casado")
    print("V - Viúvo")
    print("D - Divorciado")
    ecivil = input("Digite seu estado civil: ")
    if ecivil != "S" or ecivil != "C" or ecivil != "V" or ecivil != "D":
        print ("Estado civil inválido, tente novamente.")
        continue

    idade = input("Digite sua idade: ")
    if idade < 0 or idade > 100:
        print ("Idade inválida, tente novamente.")
        continue

    print("F - Feminino")
    print("M - Masculino")
    genero = input("Digite seu gênero: ")
    if genero != "F" or genero != "C":
        print ("Gênero inválido, tente novamente.")
        continue