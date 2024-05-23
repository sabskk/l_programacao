# Faça um algoritmo que receba como entrada o nome, cidade, estado de 50 pessoas. Após verifique a
# quantidade de pessoas que moram nas cidades:
# Criciúma
# Tubarão
# Florianopolis 

totalC = 0
totalT = 0
totalF = 0

for contador in range(10):
    nome = input("Digite seu nome: ")
    print = ("Cidades:")
    print = ("C = Criciúma / T = Tubarão / F = Florianópolis")
    cidade = input("Digite sua cidade: ").upper()
    if cidade == "C":
        totalC += 1
    if cidade == "T":
        totalT += 1
    if cidade == "F":
        totalF += 1

print("Total de pessoas de Criciúma: ",totalC)
print("Total de pessoas de Tubarãr: ",totalT)
print("Total de pessoas de Florianópolis: ",totalF)