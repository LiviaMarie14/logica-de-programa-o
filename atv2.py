valor_total = 1200.00

print(f"TABELA DE PARCELAMENTO - COMPRA R$ {valor_total:.2f}")


for quantidade_parcelas in range(1, 11):
    valor_parcela = valor_total / quantidade_parcelas
    print(f"{quantidade_parcelas}x de R$ {valor_parcela:.2f}")






