# Crie um dicionário com os nomes de times de futebol de SC, seguindo a ordem:
# Agora, inclua um novo time no final da lista 
# Mostre se o time  “Joinville” está cadastrado na lista.
# Infelizmente o time 2: “Avaí” não fazem mais parte da lista e deve ser removida.
# Ao final, mostre a lista completa de times

times = {}
contador = 0

n = int(input("Digite quantos times você deseja cadastrar: "))
for contador in range(n):
    contador += 1
    nome = input("Digite o nome do time: ")
    times[contador] = nome

print("Lista de times: ", times)

novonome = input("Digite o nome de um novo time: ")
contador += 1
times[contador] = novonome
print("Lista atualizada: ",times)

pesquisar = input("Digite o nome do time que deseja pesquisar: ")
if pesquisar in times:
    print(f"O estado {nome} ja foi cadastrado.")
else:
    print(f"O estado {nome} não foi cadastrado.")

print("Lista atual: ", times)
remover = input("Qual o nome do time que deseja alterar: ")
if remover in times:
    times.pop(remover)

print("Lista final: ", times)