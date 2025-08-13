from src.estrategia.scraper_blog import listar_concursos_blog
from src.filters import filtrar_concurso

def main():
    concursos = listar_concursos_blog()
    filtrados = [c for c in concursos if filtrar_concurso(c)]

    print(f"Encontrados {len(filtrados)} concursos:\n")
    for c in filtrados:
        print(f"📌 {c['titulo']}")
        print(f"🔗 {c['link']}")
        for k, v in c.items():
            if k not in ["titulo", "link"]:
                print(f"   {k}: {v}")
        print("-" * 50)

if __name__ == "__main__":
    main()
