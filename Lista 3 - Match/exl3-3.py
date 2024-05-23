#Uma loja está vendendo seus produtos em prestações sem juros. Faça um programa que receba o valor de uma
#compra e o numero de parcelas e após calcule e mostre o valor das prestações.

valor = float(input("Qual o valor da compra:"))
prest = int(input("Quantas prestações serão realizadas:"))
pagar = valor/prest
print("O valor a se pagar é de: R$", pagar)