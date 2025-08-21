"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:

*EQUILÁTERO: todos os lados iguais
*ISÓSCELES: dois lados iguais, um diferente
*ESCALENO: todos os lados diferentes
"""

#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

print('-=' * 20)
print("Analisador de Triângulos")
print('-=' * 20)

a: float = float(input("Primeiro segmento: "))
b: float = float(input("Segundo segmento: "))
c: float = float(input("Terceiro segmento: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    
    if a == b == c:
     tipo = "EQUILÁTERO"
    elif a == b or b == c or c == a:
     tipo = "ISÓSCELES"
    elif a != b and b != c and c != a:
     tipo = "ESCALENO"

    print(f"Os segmentos acima PODEM FORMAR um triângulo {tipo}!")

else:
     print("Os segmentos acima NÂO PODEM FORMAR triângulo")
    
