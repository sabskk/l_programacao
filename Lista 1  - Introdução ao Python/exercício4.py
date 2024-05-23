#Faca um algoritmo que receba como entrada os dados de um cliente: nome, produto, quantidade e preço.
#Calcule o valor da compra e mostre o resultado:

nome = input("Digite seu nome:")
prod = input("Digite o produto escolhido:")
quant = int(input("Quantas unidades do item serão compradas:"))
preco = float(input("Qual o preço do item:"))
pagar = (quant*preco)

print("O valor a se pagar é de", pagar)