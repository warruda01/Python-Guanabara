# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

n1: float = (float(input("Digite a primeira nota do aluno--> ")))
n2: float = (float(input("Digite a segunda nota do aluno--> ")))

print(f"A média entre {n1} e {n2} é igual a --> {(n1 + n2)/2:.2f}")