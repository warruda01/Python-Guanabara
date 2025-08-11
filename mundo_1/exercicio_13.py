#Exercício Python 13: Faça um algoritmo que leia o salário de um 
# funcionário e mostre seu novo salário, com 15% de aumento.

salario: float = float(input("Qual o salário do funcionário? "))
print(f"""Um funcionário que ganhava R${salario} passa a receber R${salario * 1.15:.2f}
com o aumento de 15%.""")