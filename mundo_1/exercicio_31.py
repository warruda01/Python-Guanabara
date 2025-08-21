#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma 
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para 
# viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia: int = int(input("Qual a distância da sua viagem? "))

print(f"Você está prestes a começar sua viagem de {distancia:.1f} Km.")
if distancia <= 200:
    passagem = distancia * 0.50
elif distancia >= 200:
    passagem = distancia * 0.45

print(f"E o preço da passagem será de R${passagem:.2f}")
