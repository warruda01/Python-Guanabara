"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com 
 a idade:
 - Até 9 anos: MIRIM
 -  Até 14 anos: INFANTIL
 -  Até 19 anos: JÚNIOR
 - Até 25 anos: SÊNIOR
 - Acima de 25 anos: MASTER"""
import datetime
ano_nasc: int = int(input("Ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nasc

if idade <= 9:
    mensagem = "MIRIM"
elif 9 < idade <= 14:
    mensagem = "INFANTIL"
elif 14 < idade <= 19:
    mensagem = "JÚNIOR"
elif 19 < idade <= 25:
    mensagem = "SÊNIOR"
elif idade > 25:
    mensagem = "MASTER"

print(f"Classificação: {mensagem}")