#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno_1: str = str(input("Aluno 1 -->"))
aluno_2: str = str(input("Aluno 2 -->"))
aluno_3: str = str(input("Aluno 3 -->"))
aluno_4: str = str(input("Aluno 4 -->"))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

random.shuffle(lista_alunos)
print(lista_alunos)