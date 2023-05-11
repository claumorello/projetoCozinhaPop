vlcompra = float(input("Digite o Valor da Compra: "))
produto = input("Digite o nome do Produto: ")

if vlcompra < 10.00:
    print("O valor da venda do produto", produto, "será de R$", (vlcompra * 0.7) + vlcompra)
if vlcompra >= 10.00 and vlcompra < 30.00:
    print("O valor da venda do produto", produto, "será de R$", (vlcompra * 0.5) + vlcompra)
if vlcompra >= 30.00 and vlcompra < 50.00:
    print("O valor da venda do produto", produto, "será de R$", (vlcompra * 0.4) + vlcompra)
else:
    vlcompra >= 50.00, print("O valor da venda do produto", produto, "será de R$", (vlcompra * 0.3) + vlcompra)