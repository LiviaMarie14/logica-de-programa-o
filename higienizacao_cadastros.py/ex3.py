sku_bruto = "  prod-1024-br  "

sku_limpo = sku_bruto.strip().upper().replace("-", "_")

print(f"Codigo formatado: {sku_limpo}")