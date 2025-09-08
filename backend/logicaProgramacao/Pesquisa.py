#pesquisar como alterar e excluir registris di arquivo txt, e criar um comentario no arquivo  do python com a explicação
#logo abaixo no mesmo arquivo criara um exemplo de sistema  de uma loja de carros onde tenha um menu no terminal, e tenha as opções de cadastrar listar alterar e excluir use as boas praticas de programação

#Como Alterar e Excluir Registros em Arquivo TXT com Python
#ALTERAR REGISTROS EM ARQUIVO TXT
#Para alterar registros em um arquivo TXT, seguimos estes passos:

#Abrir o arquivo no modo leitura ('r') para ler todo o conteúdo

#Armazenar as linhas em uma lista ou variável na memória

#Localizar o registro que deseja alterar (geralmente por um identificador único como ID)

#Modificar os dados do registro na memória

#brir o arquivo no modo escrita ('w') para reescrever todo o conteúdo

#Gravar todas as linhas no arquivo, incluindo a linha modificada

#python
# Exemplo de alteração de registro
#with open('dados.txt', 'r') as arquivo:
 #   linhas = arquivo.readlines()

# Procura e altera o registro com ID 3
#for i, linha in enumerate(linhas):
#    if linha.startswith('3|'):
#        linhas[i] = '3|NovoValor1|NovoValor2|NovoValor3\n'
#        break

# Reescreve o arquivo completo
#with open('dados.txt', 'w') as arquivo:
#    arquivo.writelines(linhas)
#EXCLUIR REGISTROS EM ARQUIVO TXT
#Para excluir registros em um arquivo TXT, seguimos estes passos:

#Abrir o arquivo no modo leitura ('r') para ler todo o conteúdo

#Filtrar as linhas removendo aquela que corresponde ao registro a ser excluído

# Abrir o arquivo no modo escrita ('w') para reescrever o conteúdo

# Gravar apenas as linhas que devem permanecer no arquivo

# python
# # Exemplo de exclusão de registro
# with open('dados.txt', 'r') as arquivo:
#     linhas = arquivo.readlines()

# # Filtra removendo o registro com ID 2
# linhas_filtradas = [linha for linha in linhas if not linha.startswith('2|')]

# # Reescreve o arquivo sem o registro excluído
# with open('dados.txt', 'w') as arquivo:
#     arquivo.writelines(linhas_filtradas)
# CONSIDERAÇÕES IMPORTANTES
# Arquivos TXT não são bancos de dados: Eles não têm estrutura para operações eficientes de atualização

# Sempre faça backup: Antes de modificar arquivos, considere fazer uma cópia de segurança

# Use identificadores únicos: É crucial ter um campo único (como ID) para localizar registros específicos

# Performance: Para arquivos muito grandes, essa abordagem pode ser lenta pois requer recriar o arquivo completo

# ALTERNATIVAS RECOMENDADAS
# Para sistemas que precisam de operações frequentes de alteração e exclusão, considere usar:

# Banco de dados SQLite (incluído no Python)

# Arquivos JSON (mais estruturados que TXT)

# Bancos de dados relacionais (MySQL, PostgreSQL) para aplicações mais complexas



# Exemplo prático de sistema de loja de carros
import os modelo = input("Modelo: ")
    ano

ARQUIVO_CARROS = "carros.txt"

def inicializar_arquivo():
    """Cria o arquivo se não existir"""
    if not os.path.exists(ARQUIVO_CARROS):
        with open(ARQUIVO_CARROS, 'w') as arquivo:
            arquivo.write("")
        print(f"Arquivo {ARQUIVO_CARROS} criado com sucesso.")

def carregar_carros():
    """Carrega todos os carros do arquivo"""
    carros = []
    try:
        with open(ARQUIVO_CARROS, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    dados = linha.split('|')
                    if len(dados) == 5:
                        carro = {
                            'id': dados[0],
                            'marca': dados[1],
                            'modelo': dados[2],
                            'ano': dados[3],
                            'preco': dados[4]
                        }
                        carros.append(carro)
    except FileNotFoundError:
        print("Arquivo não encontrado. Inicializando...")
        inicializar_arquivo()
    return carros

def salvar_carros(carros):
    """Salva a lista de carros no arquivo (sobrescreve tudo)"""
    with open(ARQUIVO_CARROS, 'w') as arquivo:
        for carro in carros:
            linha = f"{carro['id']}|{carro['marca']}|{carro['modelo']}|{carro['ano']}|{carro['preco']}\n"
            arquivo.write(linha)

def gerar_id(carros):
    """Gera um ID único para novo carro"""
    if not carros:
        return "1"
    ids = [int(c['id']) for c in carros]
    return str(max(ids) + 1)

def cadastrar_carro():
    """Cadastra um novo carro no sistema"""
    carros = carregar_carros()
    
    print("\n--- CADASTRAR CARRO ---")
    marca = input("Marca: ")