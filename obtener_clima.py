import requests

def obtener_clima(ciudad: str):
    """
    Obtiene el clima desde una API pública (wttr.in)
    """
    try:
        url = f"https://wttr.in/{ciudad}?format=3"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            return "No se pudo obtener el clima en este momento."
    except Exception as e:
        return f"Error obteniendo clima: {str(e)}"
