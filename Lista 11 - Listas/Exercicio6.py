# Faça um Programa Python que leia 4 notas, ao final mostre as notas e a média geral.

notas=[]
i = 0

while i <= 3:
    valor = float(input("Digite uma de suas notas: "))
    notas.append(valor)

media = (sum(notas)/4)

print("Suas notas foram:",notas)
print("Média:",media)