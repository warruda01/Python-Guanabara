#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
# 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada 
# Km acima do limite.

veloc: int = int(input("Qual a velocidade atual do carro? "))
print(30 * '-')
if veloc > 80:
    print(f"""MULTADO! Você excedeu o limite permitido que é de 80Km/h.
Você deve pagar uma multa de R$ {7 * (veloc - 80):.2f}!
Tenha um bom dia! Dirija com segurança!""")
else:
    print("Tenha um bom dia! Dirija com segurança!")