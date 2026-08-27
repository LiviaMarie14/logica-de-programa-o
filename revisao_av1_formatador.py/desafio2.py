def gerar_codigo(ano, cpf): 
    cpf_limpo = cpf.strip()
    tres_digitos = cpf_limpo[0:3]
    return "ALU-" + str(ano) + "-" + tres_digitos
resultado2 = gerar_codigo("2026", "456.789.123-00")
print(resultado2) 