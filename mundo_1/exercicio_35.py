#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

print('-=' * 20)
print("Analisador de Triângulos")
print('-=' * 20)

a: float = float(input("Primeiro segmento: "))
b: float = float(input("Segundo segmento: "))
c: float = float(input("Terceiro segmento: "))


if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Os segmentos acima PODEM FORMAR triângulo")
else:
     print("Os segmentos acima NÂO PODEM FORMAR triângulo")