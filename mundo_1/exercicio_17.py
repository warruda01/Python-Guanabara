#Exercício Python 17: Faça um programa que leia o comprimento do cateto 
# oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

"""cat_oposto: float = float(input("Comprimento do cateto oposto: "))
cat_adj: float = float(input("Comprimento do cateto adjacente: "))
hipotenusa: float = (cat_oposto ** 2 + cat_adj ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hipotenusa:.2f} cm.")"""


import math
cat_oposto: float = float(input("Comprimento do cateto oposto: "))
cat_adj: float = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cat_oposto, cat_adj)
print(f"A hipotenusa vai medir {hipotenusa:.2f} cm.")