# Crie um dicionário com os nomes dos estados do Brasil e sua respectiva capital, seguindo a ordem:
# Agora, inclua um novo estado e sua capital no final da lista.
# Mostre se o estado   “Distrito Federal” está cadastrado.
# Altere a capital do estado “Minas Gerais” para “Belo Horizonte”
# Ao final, mostre a lista completa de estados. 

estados = {}

n = int(input("Digite quantos estados você deseja cadastrar?: "))
for contador in range(n):
    nome = input("Digite o nome do estado: ")
    cap = input("Digite sua capital: ")
    estados[nome] = cap

print("Lista estados: ", estados)

novonome = input("Digite o nome de um novo estado: ")
novacap = input("Digite o nome de uma nova capital: ")
estados[novonome] = novacap
print("Lista atualizada: ",estados)

pesquisar = input("Digite o nome do estado que deseja pesquisar: ")
if pesquisar in estados:
    print(f"O estado {nome} ja foi cadastrado.")
else:
    print(f"O estado {nome} não foi cadastrado.")

print("Lista atual: ", estados)
alterar = input("Qual o nome do estado que deseja alterar: ")
if alterar in estados:
    novacapital = input("Digite uma nova capital: ")
    estados[alterar] = novacapital

print("Lista final: ", estados)