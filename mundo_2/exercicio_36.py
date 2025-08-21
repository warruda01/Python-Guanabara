#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a 
# compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos 
# ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo 
# será negado.

valor_casa: float = float(input("Valor da Casa: R$ "))
salario: float = float(input("Salário do comprador: R$ "))
anos: int = int(input("Quantos anos de financiamento? "))
prestacao:float = valor_casa/(12*anos)
print(f"Para pagar a casa de R$ {valor_casa:.2f} em 7 anos a prestação será de R$ {prestacao:.2f}")

if prestacao > (salario * 0.3):
    mensagem = "NEGADO"
else:
    mensagem = "CONCEDIDO"

print(f"Empréstimo {mensagem}!")