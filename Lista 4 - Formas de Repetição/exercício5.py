# Desenvolva um script Python que lê vários números positivos via teclado. Quando o número lido for -1,
# o script deve parar e exibir a soma de todos os números positivos inseridos, a média desses números, o
# menor e o maior número digitado.

soma = 0
quantidade = 0
maior = 0
menor = 999999
while True:
    numero = int(input("Digite seu número inteiro: "))
    if numero < 0:
        break
    soma = soma + numero
    quantidade = quantidade + 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print ("Quantidade de números digitados:", quantidade)
print ("Soma dos numeros:", soma)
media = soma / quantidade
print ("Maior número digitado: ",maior)
print ("Menor número digitado: ",menor)