# Construir um algoritmo que receba como entrada o nome e sexo de 10 pessoas. Após verifique a quantidade
# de pessoas de cada sexo (Masculino e Feminino).

totalM = 0
totalF = 0

for contador in range(10):
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu gênero: ").upper()
    if sexo == "M":
        totalM += 1
    if sexo == "F":
        totalF += 1
    
print("Todas as pessoas do sexo masculino: ",totalM)
print("Todas as pessoas do sexo feminino: ",totalF)