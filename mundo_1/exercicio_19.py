#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos 
# para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

aluno_1:str = str(input("Digite o nome do primeiro aluno: "))
aluno_2:str = str(input("Digite o nome do segundo aluno: "))
aluno_3:str = str(input("Digite o nome do terceiro aluno: "))
aluno_4:str = str(input("Digite o nome do quarto aluno: "))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

escolha = choice(lista_alunos)

print(f"Aluno escolhido --> {escolha}")
