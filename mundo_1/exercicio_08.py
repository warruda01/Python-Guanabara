#Exercício Python 8: Escreva um programa que leia um valor em metros e o 
# exiba convertido em centímetros e milímetros.

n: float = float(input("Digite o número em metros a ser convertido --> "))
print(f"{n}m correspondem a {n*100:.0f}cm e {n*1000:.0f}mm.")