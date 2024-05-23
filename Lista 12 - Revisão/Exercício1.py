# Utilizando a linguagem PYTHON, crie 2 listas: uma lista com  nomes dos clientes de um banco (João, Maria, etc...)
# e outra lista com saldo da conta em reais(R$) correspondentes ao cliente (1350, 3240, etc... ), e usando estruturas
# de repetição mostre os  dados da seguinte forma:

# Nome Cliente		Saldo Conta R$
# João		     	1350,00
# Maria	    		3240,00
# Etc.

# Mostrar também o maior e menor saldo da conta.

clientes = []
saldos = []

for contador in range(0,5):
    nome = input("Digite o nome do cliente:")
    clientes.append(nome)
    saldo = float(input("Digite o sado da conta: R$"))
    saldos.append(saldo)

print("-----------------------------")
print("Cliente                 Saldo")
print("-----------------------------")

for contador in range(0,5):
    print((clientes[contador]),"             ",(saldos[contador]))

print("-----------------------------")

print("Maior saldo da conta: R$",max(saldos))
print("Menor saldo da conta: R$",min(saldos))