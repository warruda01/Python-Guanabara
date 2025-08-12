#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num: str = str(input("Informe um número de 0 a 9999 --> "))

lista_num: list = num
print(f"Analisando o número {num}")
print(f"Unidade --> {lista_num[3]}")
print(f"Dezena --> {lista_num[2]}")
print(f"Centena --> {lista_num[1]}")
print(f"Milhar --> {lista_num[0]}")

print(50 * '-')

#Outra resolução:
num = int(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Analisando o número {num}")
print(f"Unidade --> {u}")
print(f"Dezena --> {d}")
print(f"Centena --> {c}")
print(f"Milhar --> {m}")