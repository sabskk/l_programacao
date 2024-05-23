# Faça um Programa Python que crie 3 listas: uma lista com  nomes de frutas (laranja, banana, etc...) e outra lista
# com quantidade em estoque correspondente as frutas (35,20, etc.) e uma terceira lista correspondendo o preço do
# quilo da fruta (4.25,  3,75, etc.) usando estruturas de repetição mostre os  dados da seguinte forma:

# Fruta		Quantidade		Preço R$
# Laranja		35			4.25
# Banana		20			3.75
# Etc.

# Mostrar também as frutas com maior e menor quantidade em estoque.
# Mostrar a soma total das quantidades das frutas.

frutas = []
qtdes = []
precos = []

maiorqtde = 0
nomemaior = ""
menorqtde = 999
nomemenor = ""

for contador in range (0,5):
    nome = input("Digite o nome da fruta:")
    frutas.append(nome)
    qtde = int(input("Digite a quantidade:"))
    qtdes.append(qtde)
    preco = float(input("Digite o preço: R$"))
    precos.append(preco)

    if qtde > maiorqtde:
        maiorqtde = qtde
        nomemaior = nome

    if qtde < menorqtde:
        menorqtde = qtde
        nomemenor = nome

print("-------------------------------------")
print("Fruta   |   Quantidade   |   Preço R$")
print("-------------------------------------")

for contador in range(0,5):
    print((frutas[contador]),"   ",(qtdes[contador],"   ",(precos[contador])))
    
print("-------------------------------------")

print("Fruta de maior quantidade:",nomemaior,"R$:",maiorqtde)
print("Fruta de menor quantidade:",nomemenor,"R$:",menorqtde)