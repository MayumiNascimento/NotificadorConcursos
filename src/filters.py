# FILTROS PARA BUSCA DE CONCURSOS, EDITA-LOS NOS RESPECTIVOS ARRAYS
# Áreas específicas para EXCLUIR
AREAS = ["GCM", "Policia", "Guarda"]

# Estado (UF)
ESTADOS = ["SP"]

def filtrar_concurso(concurso: dict) -> bool:
    """
    Retorna True se o concurso atender aos filtros definidos.
    """
    titulo = concurso["titulo"].lower()
    texto_completo = (concurso['titulo'] + " " + " ".join(f"{k}: {v}" for k, v in concurso.items())).lower()

    # Se tiver áreas definidas, verifica
    if AREAS and any(area.lower() in texto_completo for area in AREAS):
        return False
    
    # Verifica estado (no título apenas)
    if not any(f" {estado.lower()}" in titulo or titulo.endswith(f" {estado.lower()}") for estado in ESTADOS):
        return False
    return True