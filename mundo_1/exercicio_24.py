#Exercício Python 24: Crie um programa que leia o nome de uma cidade 
# diga se ela começa ou não com o nome “SANTO”.

cidade: str = str(input("Digite o nome da cidade --> ")).strip().upper()

separa_cidade = cidade.split()

if separa_cidade[0] in 'SANTO':
    print("Positivo. Começa com Santo")
else:
    print("Negativo. Não começa com Santo")

#Outra resolução:
print('-' * 30)
print(cidade[:5].upper() == 'SANTO')