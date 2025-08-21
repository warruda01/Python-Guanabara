#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora 
# exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá 
# mostrar o tempo que falta ou que passou do prazo.

import datetime
ano_nascimento: int = int(input("Ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade_atual = ano_atual - ano_nascimento
idade_alistamento = 18
print(f"Quem nasceu em {ano_nascimento} tem {idade_atual} anos de idade em {ano_atual}.")
if idade_atual > idade_alistamento:
    print(f"Você deveria ter se alistado há {idade_atual - idade_alistamento} ano(s)")
    print(f"Seu alistamento foi em {ano_nascimento + idade_alistamento}")
elif idade_atual < idade_alistamento:
    print(f"Ainda faltam {idade_alistamento - idade_atual} anos.")
    print(f"Seu alistamento será em {ano_nascimento + idade_alistamento}")
elif idade_atual == idade_alistamento:
    print("Você deve se alistar IMEDIATAMENTE!")