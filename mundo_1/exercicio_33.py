# Exercício Python 33: Faça um programa que leia três números e mostre qual é 
# o maior e qual é o menor.

primeiro: int = int(input("Primeiro valor: "))
segundo: int = int(input("Segundo valor: "))
terceiro: int = int(input("Terceiro valor: "))

menor = primeiro
maior = primeiro

if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

#Outra Resolução
#Verificando o menor
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

#Verificando o maior
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    menor = segundo
if terceiro > primeiro and terceiro > segundo:
    menor = terceiro

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')