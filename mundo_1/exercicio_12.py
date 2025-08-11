#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e 
# mostre seu novo preço, com 5% de desconto.

preco: float = float(input("Qual o preço do produto? "))
print(f"""O produto que custava R$ {(preco):.2f}, vai custar R$ {(preco * 0.95):.2f} na
promoção com 5% de desconto.""")