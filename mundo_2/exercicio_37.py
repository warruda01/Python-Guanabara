#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal 
# e 3 para hexadecimal.
import math
numero: int = int(input("Digite um número inteiro: "))
print("Escolha uma base pasra sua conversão:")
print("[ 1 ] - converter para BINÁRIO")
print("[ 2 ] - converter para OCTAL")
print("[ 3 ] - converter para HEXADECIMAL")
base:int = int(input("Sua opção: "))

if base == 1:
    print(f"{numero:b}")
elif base == 2:
    print(f"{numero:o}")
elif base == 3:
    print(f"{numero:X}")
else: 
    print("Opção inválida")