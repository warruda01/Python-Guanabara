"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma 
pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo 
com a tabela abaixo:

*IMC abaixo de 18,5: Abaixo do Peso
*Entre 18,5 e 25: Peso Ideal
*25 até 30: Sobrepeso
*30 até 40: Obesidade
*Acima de 40: Obesidade Mórbida"""

peso: float = float(input("Qual seu peso (Kg)? "))
altura: float = float(input("Qual sua altura (m)? "))
imc = peso / (altura**2)
print(f"O IMC desta pessoa é de: {imc:.1f}")

if imc < 18.5:
    msg = "Abaixo do Peso"
elif 18.5 <= imc < 25:
    msg = "Peso Ideal"
elif 25 <= imc < 30:
    msg = "Sobrepeso"
elif 30 <= imc < 40:
    msg = "Obesidade"
elif imc > 40:
    msg = "Obesidade Mórbida"

print(f"Resultado: {msg}!")
