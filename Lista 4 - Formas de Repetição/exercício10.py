# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite seu nome de usuário: ")
while True:
    senha = input("Digite uma senha: ")
    if senha == nome:
        print ("Senha não deve ser igual ao nome de usuário, tente novamente.")
        continue
    else: 
        print ("Nome de usuário: ",nome)
        print ("Senha: ",senha)