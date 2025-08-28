#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando um laço for.

n: int = int(input("Digite um número inteiro: "))

for c in range (1, 11):
    print(f"{n} x {c:2} = {n *c}")
print(10 * '-')