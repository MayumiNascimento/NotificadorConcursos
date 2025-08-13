import requests
from bs4 import BeautifulSoup

URL = "https://www.estrategiaconcursos.com.br/blog/concursos-abertos/"

def listar_concursos_blog():
    r = requests.get(URL)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    concursos = []

    # Percorre todos os títulos de concursos
    for titulo_tag in soup.select("h3.wp-block-heading"):
        a_tag = titulo_tag.find("a")
        if not a_tag:
            continue

        titulo = a_tag.get_text(strip=True)
        link = a_tag["href"]

        # Pega a lista de informações logo depois do título
        ul_tag = titulo_tag.find_next_sibling("ul")
        info = {}
        if ul_tag:
            for li in ul_tag.find_all("li"):
                label_tag = li.find("strong")
                if label_tag:
                    label = label_tag.get_text(strip=True).replace(":", "")
                    valor = li.get_text(strip=True).replace(label_tag.get_text(strip=True), "").strip()
                    info[label] = valor

        concursos.append({
            "titulo": titulo,
            "link": link,
            **info
        })

    return concursos
