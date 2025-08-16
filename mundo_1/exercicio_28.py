#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep #importando a biblioteca para o timer

print('-=-' * 30)
print('Vou pensar um um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)

num_usuario: int = int(input("Em que número eu pensei? --> ")) #Jogador tenta adivinhar
print("PROCESSANDO...")

sleep(2) #usando o timer

num_comp: int = randint(0, 5)
if num_usuario != num_comp:
    print(f"GANHEI! Eu pensei no número {num_comp} e não no {num_usuario}!")
else:
    print(f"PARABÉNS! Você conseguiu me vencer!")