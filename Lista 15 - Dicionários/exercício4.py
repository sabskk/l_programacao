# Desenvolva um script em linguagem Python, utilizando Dicionários, que solicite ao usuário inserir o nome de 05
# livros e seus respectivos autores e os mostre na tela.

dicionario = {}

for range in range(0, 5):
    título = input("Digite o título do livro: ")
    auto = float(input("Digite o nome do autor do livro: "))
    dicionario[título] = auto

print(dicionario)