#Exercício Python 14: Escreva um programa que converta uma temperatura 
# digitando em graus Celsius e converta para graus Fahrenheit.

celsius: float = float(input("Digite a temperatura em °C: "))
print(f"A temperadura de {celsius}°C corresponde a {(celsius * 1.8) + 32:.1f}°F")