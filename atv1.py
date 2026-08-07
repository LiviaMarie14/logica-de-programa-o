qtd_itens = int(input("quantidade de itens"))
total_compra = 0.0

for i in range (1, qtd_itens + 1):
    preco = float(input(f"Preco do iten {i}: R$ "))
    total_compra += preco
    media_por_item = total_compra / qtd_itens if qtd_itens > 0 else 0

    print(f"total da compra: R$ ")