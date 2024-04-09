import random
import string
import requests
import socket
from colorama import init, Fore

init(autoreset=True)

# Chave interna fixa
chave_interna = "felipedev"

def verificar_conexao_rede():
    try:
        # Faz uma conexão com um servidor externo para verificar a conectividade de rede
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def obter_key():
    if verificar_conexao_rede():
        # Se estiver conectado à internet, obtém a chave do site
        url = 'https://raw.githubusercontent.com/livehostne/keyf/main/key'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                key = response.text.strip()
                return key
            else:
                print(f"{Fore.RED}Erro ao obter a chave do site. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"{Fore.RED}Erro ao obter a chave do site: {e}")
            return None
    else:
        # Se não estiver conectado à internet, retorna a chave interna
        return chave_interna

def gerar_usuario(tamanho, tipo):
    if tipo == 'numeros':
        caracteres = string.digits
    elif tipo == 'letras':
        caracteres = string.ascii_letters
    else:
        caracteres = string.ascii_letters + string.digits
    
    usuario = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return usuario

def gerar_senha(tamanho, tipo):
    if tipo == 'numeros':
        caracteres = string.digits
    elif tipo == 'letras':
        caracteres = string.ascii_letters
    else:
        caracteres = string.ascii_letters + string.digits
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_lista(quantidade, tamanho_usuario, tamanho_senha, tipo_usuario, tipo_senha, diretorio, nome_arquivo):
    lista = []
    for _ in range(quantidade):
        usuario = gerar_usuario(tamanho_usuario, tipo_usuario)
        senha = gerar_senha(tamanho_senha, tipo_senha)
        lista.append(f"{usuario}:{senha}")
    
    arquivo_path = diretorio + nome_arquivo
    with open(arquivo_path, 'w') as arquivo:
        for item in lista:
            arquivo.write(item + '\n')
    
    return arquivo_path

print(f"{Fore.GREEN}FELIPE GERADOR")

# Verifica se a chave pode ser obtida
key = obter_key()

if key:
    print(f"{Fore.GREEN}Chave obtida com sucesso: {key}")
    quantidade = int(input("Quantidade de usuários e senhas a serem gerados: "))
    tamanho_usuario = int(input("Tamanho do usuário (em caracteres): "))
    tamanho_senha = int(input("Tamanho da senha (em caracteres): "))

    tipo_usuario = input("Tipo de caracteres para o usuário (letras/numeros/ambos): ").lower()
    while tipo_usuario not in ['letras', 'numeros', 'ambos']:
        print("Opção inválida! Por favor, digite 'letras', 'numeros' ou 'ambos'.")
        tipo_usuario = input("Tipo de caracteres para o usuário (letras/numeros/ambos): ").lower()

    tipo_senha = input("Tipo de caracteres para a senha (letras/numeros/ambos): ").lower()
    while tipo_senha not in ['letras', 'numeros', 'ambos']:
        print("Opção inválida! Por favor, digite 'letras', 'numeros' ou 'ambos'.")
        tipo_senha = input("Tipo de caracteres para a senha (letras/numeros/ambos): ").lower()

    diretorio_padrao = "/sdcard/combo/"
    usar_diretorio_padrao = input(f"Deseja usar o diretório padrão ({diretorio_padrao})? (sim/não): ").lower()

    if usar_diretorio_padrao == 'sim':
        diretorio = diretorio_padrao
    else:
        diretorio = input("Digite o diretório onde deseja salvar a lista (ex: /caminho/para/salvar/): ")

    nome_arquivo = input("Digite o nome do arquivo para salvar a lista (com a extensão .txt): ")

    lista_usuarios_senhas = gerar_lista(quantidade, tamanho_usuario, tamanho_senha, tipo_usuario, tipo_senha, diretorio, nome_arquivo)

    print(f'Lista de usuários e senhas gerada com sucesso em "{lista_usuarios_senhas}"!')
else:
    print(f"{Fore.RED}Não foi possível obter a chave. Verifique sua conexão com a internet.")
