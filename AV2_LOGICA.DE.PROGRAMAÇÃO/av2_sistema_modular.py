# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: 
# Data: 
# Link do Repositório: 
# ==============================================================================

# Lista inicial de dados brutos
# Formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
    "  Marinette do panchang;estilista;75395185264  ",
    "  Chloe Borjouar;modelo em teste;96385274197  ",
    "  Adrien Agreste;pesquisador de tendências;1598627518246  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    Recebe uma string, remove espaços das pontas e
    converte o texto para letras maiúsculas.
    """
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    Recebe um telefone ou código, remove espaços das pontas
    e utiliza fatiamento para extrair os dois primeiros dígitos.
    """
    dado_limpo = dado.strip()
    codigo = dado_limpo[0:2]
    return codigo


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    Percorre a lista de cadastros usando FOR, separa os dados
    com SPLIT, utiliza as funções anteriores e exibe os
    resultados formatados.
    
    Retorna a quantidade total de registros processados.
    """
    total_processado = 0

    for dado in lista_dados:
        # Separa o nome, cargo e telefone usando o ponto e vírgula
        partes = dado.strip().split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        # Utiliza as funções de tratamento
        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        # Exibe os dados formatados
        print(f"Nome: {nome_formatado}")
        print(f"Cargo/Setor: {cargo_formatado}")
        print(f"DDD/Código: {ddd}")
        print("-" * 50)

        total_processado += 1

    return total_processado


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    # Chama a Função 3 e armazena o retorno
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Exibe a quantidade total de registros processados
    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


# ------------------------------------------------------------------------------
# Execução do programa
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
