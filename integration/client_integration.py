import requests


def call_cnpj_api(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)
    return response.json()
