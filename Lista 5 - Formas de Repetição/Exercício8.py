# Faça um algoritmo que leia os dados de uma pesquisa, sobre as marcas de automóveis mais vendidas no mundo.
# Como entrada de dados. leia o nome do proprietário e a marca do automóvel (total de 500 pessoas). Após
#verificar o total de cada marca:

totalC = 0
totalV = 0
totalF = 0
totalH = 0
totalFo = 0

for contador in range(10):
    nome = input("Digite seu nome: ")
    print = ("Marcas:")
    print = ("C = Chevrolet / V = Volkswagen / F = Fiat / H = Hyundai / FO = Ford")
    curso = input("Digite a marca de seu carro: ").upper()
    if curso == "C":
        totalC += 1
    if curso == "V":
        totalV += 1   
    if curso == "F":
        totalF += 1
    if curso == "H":
        totalH += 1 
    if curso == "FO":
        totalFo += 1 

print("Total de modelos Chevrolet: ",totalC)
print("Total de modelos Volkswagen: ",totalV)
print("Total de modelos Fiat: ",totalF)
print("Total de modelos Hyundai: ",totalH)
print("Total de modelos Ford: ",totalFo)