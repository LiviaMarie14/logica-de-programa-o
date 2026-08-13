email = input("digite seu e-mail (nome.sobrenome@escola.com): ")

primeiro_nome = email[0:5]
dominio = email[13:]

print(f"primero nome extraido: {primeiro_nome}")
print(f"dominio extraido: {dominio}")