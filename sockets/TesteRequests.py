import requests

resposta = requests.get("https://www.uol.com.br")

print(resposta.text)