#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print("Suas opções: ")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
jogada: int = int(input("Qual é a sua jogada? "))

print("JO")
print("KEN")
print("PO!!!")

print(15 * '-=')
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogada]}")
print(15 * '-=')

if jogada == computador:
    print("EMPATE")
elif (jogada == 0 and computador == 2) or (jogada == 1 and computador == 0) or (jogada == 2 and computador == 1):
    print("JOGADOR VENCE")
elif (jogada == 0 and computador == 1) or (jogada == 1 and computador == 2) or (jogada == 2 and computador == 0):
    print("COMPUTADOR VENCE")



    