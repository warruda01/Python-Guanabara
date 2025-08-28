#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, 
# desconsidere-o.

soma = 0
quant: int = int(input("Quantos números serão lidos: "))
cont = 0
for n in range (1, quant+1):
    num = int(input(f"Digite o número {n} --> "))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f"Você informou {cont} números PARES e a soma foi {soma}.")    