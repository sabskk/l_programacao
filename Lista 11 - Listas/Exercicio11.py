# Faça um Programa Python que peça a idade de 10 pessoas, armazene  a informação na sua respectiva lista. Imprima a
# lista das idades na ordem menor para maior.

idades = []
i = 0

while i <= 4:
    i += 1
    valor = int(input("Insira a nota aluno:"))
    idades.append(valor)

print("Lista de idades:",idades)

idades.sort(reverse=False)
print("Lista de idades - Decrescente:",idades)

idades.sort(reverse=True)
print("Lista de idades - Crescente:",idades)