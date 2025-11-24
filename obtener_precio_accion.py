import requests

def obtener_precio_accion(ticker: str):
    """
    Obtiene el precio actual de una acción usando la API pública de Yahoo Finance.
    """
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        respuesta = requests.get(url).json()

        precio = respuesta["chart"]["result"][0]["meta"]["regularMarketPrice"]
        moneda = respuesta["chart"]["result"][0]["meta"]["currency"]

        return f"El precio actual de {ticker.upper()} es {precio} {moneda}"
    except Exception as e:
        return f"No se pudo obtener el precio de la acción: {str(e)}"
