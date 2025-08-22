"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um 
produto, considerando o seu preço normal e condição de pagamento:

* à vista dinheiro/cheque: 10% de desconto
* à vista no cartão: 5% de desconto
* em até 2x no cartão: preço formal 
* 3x ou mais no cartão: 20% de juros"""

print("=" * 20+"LOJAS WILBER"+"=" * 20)
compras: float = float(input("Preço das compras: R$ "))

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão """)
opcao: int = int(input("Qual é a opção? "))

if opcao == 1:
    total = (compras * 0,1) - compras
    print(f"Sua compra de R$ {compras:.2f} vai custar R$ {total:.2f}")
elif opcao == 2:
    total = (compras * 0.05) - compras
    print(f"Sua compra de R$ {compras:.2f} vai custar R$ {total:.2f}")
elif opcao == 3:
    parcelas = compras / 2
    print(f"Sua compra de R$ {compras:.2f} será paga em 2x de {parcelas}")

elif opcao == 4:
    vezes: int = int(input("Quantas parcelas? "))
    juros = compras * 0.20
    parcelas = (compras + juros) / vezes
    print(f"Sua compra será parcelada em {vezes} de R$ {parcelas:.2f} COM JUROS.")
    print(f"Sua compra de R$ {compras:.2f} vai custar R$ {compras + juros:.2f} no final")
