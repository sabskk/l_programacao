# Crie um script em linguagem Python que leia dois vetores com 5 elementos cada. Gere um terceiro vetor de 10
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Exibir na tela
#todos os vetores em linhas separadas.

A = []
B = []
C = []

i = 0
listac = 0

while i <= 4:
    valor1 = int(input("Digite um valor - Lista A: "))
    A.append(valor1)
    valor2 = int(input("Digite um valor - Lista B: "))
    B.append(valor2)

    C.insert(listac, valor1)
    listac += 1
    C.insert(listac, valor2)
    listac += 1

print("Lista A:",A)
print("Lista B:",B)
print("Lista C - Resultante:",C)