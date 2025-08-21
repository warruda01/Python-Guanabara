#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule 
# sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO
#– Média
#– Média 7.0 ou superior: APROVADO

n1: float = float(input("Digite a primeira nota --> "))
n2: float = float(input("Digite a segunda nota --> "))
media = (n1 + n2) / 2

if media >= 7.0:
    print(f"""Tirando {n1} e {n2} a média do aluno é {media}.
O aluno está APROVADO.""")

elif 7.0 > media >= 5:
        print(f"""Tirando {n1} e {n2} a média do aluno é {media}.
O aluno está DE RECUPERAÇÃO.""")

elif media < 5.0:
        print(f"""Tirando {n1} e {n2} a média do aluno é {media}.
O aluno está REPROVADO.""")