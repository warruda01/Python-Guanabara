Exercícios resolvidos do Curso de Python do Guanabara - Mundo 1


Exercício 4: 
    Tipos primitivos
    Abordadis na Variável:
        Só tem espaços?
        É um número?
        É alfabético?
        É alfanumérico?
        Esta em maiúsculo?
        Está em minúsculo?
        Está Capitalizada?

Exercício 5:
        
        Fornecendo um número devolve o antecessor e o sucessor

Exercício 6:

        Fornecendo um número devolve dobro, triplo e raíz quadrada. Para arredondamento usamos: "raíz quadrada é {n ** (1/2):.2f}"

Exercício 7:

        Dadas 2 notas, devolve a média do aluno

Exercício 8:

        Fornecendo um número converte para cm e mm

Exercício 9:

        Fornecendo um número devolve a tabuada
    
Exercício 10:

        Fornecendo um valor em real devolve em dólar
    
Exercício 11:

        Fornecendo a altura e largura de uma parede, calcula a quantidade de tinta a ser usada

Exercício 12:

        Lê o valor de um produto e devolve com 5% de desconto

Exercício 13:

        Lê o valor do salário de um funcionário e devolve com aumento de 15%

Exercício 14:

        Lê a temperatura em Celsius e retorna em F

Exercício 15:

        Aluguel de carros = Recebe a quantidade de dias e km rodados e calcula o valor do aluguem a pagar

Exercício 16:

        Dado um número real devolve a parte inteira do mesmo. Usando // 1 ou int(num)

Exercício 17:

        Lê o cateto oposto, adjacente e calcula a hipotenusa.

Exercício 18:

        Lê um ângulo e devolve o seno, cosseno e tangente usando as funções de math.


Exercício 19:
        Pede o nome de 4 alunos coloca-os em uma lista faz sorteio de 1 nome: escolha = random.choice(lista_alunos)

Exercício 20:

        Pede o nome de 4 alunos coloca-os em uma lista e refaz a ordem da lista aleatoriamente:random.shuffle(lista_alunos)

Exercício 21:

        Toca um arquivo MP3.

Exercício 22:

        Lê o nome completo de uma pessoa e O mostra todas as letras maiúsculas, minúsculas, conta os caracteres, Mostra somente o primeiro nome e quantos caracteres há no primeiro nome.
        - nome.upper()
        - nome.lower()
        - nome_sem_espaco = nome.replace(" ", "")
        - len(nome_sem_espaco)
        - nome_cortado = nome.split()
        - len(nome_cortado[0])

Exercício 23:

        Ao entrar com um número entre 0 e 9999, devolve a unidade, dezena, centena e milhar separadamente.
        Duas resoluções:
        - Ou transforma em uma lista
        - Ou retira a parte inteira do número dividindo por 1, 10, 100, 1000 de pois calcula o resto dividindo por 10. 
                u = num // 1 % 10
                d = num // 10 % 10
                c = num // 100 % 10
                m = num // 1000 % 10

Exercício 24: 

        Le o nome de uma cidade e diz se ela começa ou não com o nome “SANTO”.
        Duas resoluções:
        - Ou divide os nomes da cidade e testa se a posição 0 está em 'SANTO'
        - Ou faz o teste se os primeiros 5 caracteres correspondem a 'SANTO' após passá-los a maíusculo.
        
Exercício 25:
        Le o nome de uma pessoa e diz se ele tem “SILVA”.
        Duas resoluções:
        - Divide a sttring em uma lista e usa um FOR percorrendo todas as posições após transformar em upper()
        - Ou faz verifica através de "in" se a palavra 'silva' está na string

Exercício 26:
        Lê uma frase e conta quantas vezes a letra 'A' aparece, qual a posição da primeira vez
        que aparece (usando .format(frase.find('A')+1)) e a ultima posição (usando .format(frase.find('A')+1)).

Exercício 27:
        Lê um nome completo e mostra o primeiro e último nome. Usa o split() para transformar
        em uma lista e nome[0] e nome[len(nome)-1]

Exercício 28:
        Pede um número para usuário e verifica se é o mesmo usado pelo computador.
        Uso da randomint e sleep (timer)

Exercício 29:
        Lê a velocidade de um carro e devolve o valor da multa conforme os KM
        além da vel permitida. Usa IF

Exercício 30:
        Lê um número qualquer e responde se é par ou ímpar usando IF e % (resto da divisão)

Exercício 31
        recebe a kilometragem da viagem para determinar o valor da passagem usando IF

Exercício 32
        Calcula se o ano fornecido é bissexto. Se for fornecido o 0, é calculado o ano atual usando ano = date.today().year.
        Fórmula ano bissexto: if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
