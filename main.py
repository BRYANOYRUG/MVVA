import requests
from bs4 import BeautifulSoup

#minecraft version verifier api
#MVVA
url = "https://minecraft.wiki/w/Bedrock_Dedicated_Server"

print("v0.1 \nBy BMRL\n")
print(f"Requisitando na {url} ...")
html_txt = requests.get(url, timeout=20)
html_txt.raise_for_status()

html = BeautifulSoup(html_txt.text, "html.parser")

release = html.find("b", string="Release:")
versao = html.find("a", class_="mw-redirect")

print(f"parentes: {versao.find_previous_sibling("b")}")

if release.find_next_sibling() == versao:
    print(f"Versão Minecraft BDS release: {versao.get_text(strip=True)}")

else:
    print("Versão não encontrada")

input("Aperte enter para fechar.")