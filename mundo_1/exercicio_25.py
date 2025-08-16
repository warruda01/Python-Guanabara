nome: str = str(input("Qual é seu nome completo? ")).strip().upper()

cortado: list = nome.split() #Transforma a String em uma lista

for n in cortado:
    if n == 'SILVA':
        resultado = True
    else:
        resultado = False

print(f"Seu nome tem Silva? {resultado}")


#Outra Resolução:
#nome: str = str(input("Qual é seu nome completo? ")).strip()
#print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))