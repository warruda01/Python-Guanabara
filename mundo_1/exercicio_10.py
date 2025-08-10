#Exercício Python 10: Crie um programa que leia quanto 
# dinheiro uma pessoa tem na 
# carteira e mostre quantos dólares ela pode comprar.

real: float = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar: float = float(input("Qual o valor do dólar hoje? R$ "))

print(f"Com R${real:.2f} você tem U${real/dolar:.2f} na carteira")
