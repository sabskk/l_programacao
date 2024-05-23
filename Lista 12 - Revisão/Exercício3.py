# Faça um Programa Python que leia uma frase (caracteres), e diga quantas vogais e consoantes foram lidas. Mostre a
# lista ao final.

TotalConsoantes = 0
TotalVogais = 0

frase = input("Digite uma frase:").upper()

frase2 = frase.replace(" ","")

for contador in frase2:
    if contador == "A" or contador == "E" or contador == "I" or contador == "O" or contador == "U":
        TotalVogais += 1
    else:
        TotalConsoantes += 1

print("Frase digitada:",frase)
print("Total de Vogais:",TotalVogais)
print("Total de Consoantes:",TotalConsoantes)