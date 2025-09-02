# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão 
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(30 * '-')
print('     10 TERMOS DE UMA PA     ')
print(30 * '-')

primeiro: int = int(input("Primeiro Termo: "))
razao: int = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for n in range(primeiro, decimo + razao, razao):
    print(f'{n} -> ', end='')

print('ACABOU')