#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. 
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1: int = int(input("Primeiro numero: "))
n2: int = int(input("Segundo numero: "))

if n1 > n2:
    print("O primeiro valor é maior.")
elif n1 < n2:
    print("O segundo número é maior.")
elif n1 == n2:
    print("Os dois valores são iguais")