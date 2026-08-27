def formatar_citação(nome_completo): 
    partes = nome_completo.strip().split()
    sobrenome = partes[-1].upper()
    primeiro_nome = " ".join(partes[:-1])

    return sobrenome + ", " + primeiro_nome

resultado1 = formatar_citação("Carlos Eduardo Andrade")
print(resultado1) 
