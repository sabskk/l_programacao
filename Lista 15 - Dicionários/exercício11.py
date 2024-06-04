# Crie um dicionário com os nomes de atletas famosos, seguindo a ordem:
# Agora, inclua um novo atleta no final da lista 
# Mostre se o atleta “Roger Federer” : “Tênis” está cadastrado. 
# Infelizmente o atleta “Tiger Woods” : “Golfe”  não faz mais parte da lista e deve ser removido.
# Ao final, mostre a lista completa de atletas.

atletas = {}
contador = 0

n = int(input("Digite quantos atletas você deseja cadastrar: "))
for contador in range(n):
    nome = input("Digite o nome do atleta: ")
    esp = input("Digite o nome do esporte: ")
    atletas[nome] = esp

print("Lista atletas: ", atletas)

novonome = input("Digite o nome de um novo atleta: ")
novoesp = input("Digite o nome de um novo esporte: ")
atletas[novonome] = novoesp
print("Lista atualizada: ",atletas)

pesquisar = input("Digite o nome do atleta que deseja pesquisar: ")
if pesquisar in atletas:
    print(f"O atleta {nome} ja foi cadastrado.")
else:
    print(f"O atleta {nome} não foi cadastrado.")

print("Lista atual: ", atletas)
remover = input("Qual o nome do atleta que deseja remover: ")
if remover in atletas:
    atletas.pop(remover)

print("Lista final: ", atletas)