#Exercício Python 11: Faça um programa que leia a 
# largura e a altura de uma parede em metros, calcule a 
# sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada 
# litro de tinta pinta uma área de 2 metros quadrados.

largura: float = float(input("Qual a largura da parede? "))
altura: float = float(input("Qual a altura da parede? "))
area = largura * altura
print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.3f}m2")

print(f"São necessários {(area / 2):.4f} litros de tinta para pintar toda a parede.")