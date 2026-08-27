brutos = [
    "  MARIA DA SILVA  ",
    "joao.souza@EMAIL.com ",
    "  RUA DAS FLORES, No 123  ",
    "  000.111.222-33 "
    "CARLOS.ROCHA@ESCOLA.ORG  ",
    "  AV. CENTRAL, No 450"

]

dados_limpos = []
for item in brutos: 
    texto = item.strip()

if "@" in texto:
    texto = texto.lower()
else: 
    texto = texto.replace("No", "Número")
texto = texto.replace(".", "").replace("-", "")

dados_limpos.append(texto)

for dado in dados_limpos:
        print("-", dado)