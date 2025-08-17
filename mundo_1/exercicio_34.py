#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario: float = float(input("Qual é o salário do funcionário? R$ "))

if salario > 1250:
    mensagem = f"Quem ganhava R$ {salario:,.2f} passa a ganhar R$ {salario*1.10:,.2f} agora."
elif salario <= 1250 and salario > 0:
    mensagem = f"Quem ganhava R$ {salario:,.2f} passa a ganhar R$ {salario*1.15:,.2f} agora."
else:
    mensagem = "Valor inválido"

print(mensagem)