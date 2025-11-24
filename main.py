from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar

def main():
    print("=== Chatbot iniciado ===")

    ciudad = sanitizar(input("Ingresa una ciudad para consultar el clima: "))
    resultado_clima = obtener_clima(ciudad)
    print("Respuesta del clima:", resultado_clima)

    ticker = sanitizar(input("Ingresa un ticker para consultar el precio de la acción: "))
    resultado_precio = obtener_precio_accion(ticker)
    print("Respuesta del precio:", resultado_precio)

if __name__ == "__main__":
    main()
