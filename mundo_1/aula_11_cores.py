"""
[Style:Texto:Back]
#Style: 
0 - None
1 - Bold
4 - Underline
7 - Negative

#Text:
30 - White
31 - Red
32 - Green
33 - Yellow
34 - Blue
35 - Purple
36 - Cyan
37 - Gray

#Back
Same

"""

print('\033[31;43mOlá, Mundo!\033[m') #\033[m' para a faixa não ir até o fim da linha
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[7mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m') #Colocando um 7 no início ele inverte (Negative)

print('-' * 30)
a = 3
b = 5
print(f"Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m \033[35m!!!\033[m ")

print('-' * 30)
#Outra Maneira:
nome = 'Wilber'
print('Olá, Muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

print('-' * 30)
#Outra Maneira:
nome = 'Wilber'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}  
print('Olá, Muito prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))