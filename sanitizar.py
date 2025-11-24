def sanitizar(texto: str) -> str:
    """
    Limpia y normaliza un texto antes de usarlo.
    """
    if not isinstance(texto, str):
        return ""

    return texto.strip().lower()
