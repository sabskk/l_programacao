# Faça um Programa Python que leia uma sequencia de números inteiros e armazene-os numa lista. Armazene os números
# pares na lista PAR e os números impares na lista IMPAR. Imprima ao final as listas armazenadas.

numeros = []
pares = []
impares = []
i = 0

while i <= 4:
    valor = int(input("Digite um valor inteiro: "))
    numeros.append(valor)

    if (valor % 2) == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Números digitados: ",numeros)
print("Números pares: ",pares)
print("Números ímpares: ",impares)