#Exercício Python 16: Crie um programa que leia um número Real qualquer 
# pelo teclado e mostre na tela a sua porção Inteira.

valor: float = float(input("Digite um valor --> "))
print(f"O valor digitado foi {valor} e a sua porção inteira é {valor // 1:.0f}")
print(f"O valor digitado foi {valor} e a sua porção inteira é {int(valor)}")