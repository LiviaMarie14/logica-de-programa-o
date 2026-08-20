CPF = " 123.456.789-00 "
telefone = "(11) 99999-8888"

cpf_limpo = CPF.strip().replace()
telefone_limpo = telefone.strip().replace("-","()")

print("CPF limpo:", {cpf_limpo})
print("telefone limpo:", {telefone_limpo})