#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

nome:str = str(input("Digite seu nome completo --> "))

print("Seu nome em maiúsculas é", nome.upper())
print("Seu nome em minúsculas é", nome.lower())

# para deduzir os espaços poderia ser:
#len(nome) - nome.count(' ')
nome_sem_espaco = nome.replace(" ", "")
print("Seu nome tem ao todo", len(nome_sem_espaco), "letras")
nome_cortado = nome.split()
print("Seu primeiro nome é", (nome_cortado[0]), "e ele tem", len(nome_cortado[0]), "letras.")