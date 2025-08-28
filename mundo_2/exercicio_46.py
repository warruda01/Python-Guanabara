#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos 
# de artifício, # indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
cont = 10


while cont >= 0:
    print (cont)
    sleep(0.5)
    cont -=1

print("BUM! BUM! POOOOW")

print(10 * '-')

for n in range (10, -1, -1): #Começa em 10, vai até 0 pois o -1 é ignorado, pulando de 1 em 1
    print (n)
    sleep(0.5)

print("BUM! BUM! POOOOW")