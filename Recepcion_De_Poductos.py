stock = {}
rechazos = []

def update_stock(guia):
    
    print(f"\nActualizando stock según la guía {guia}...")
    try:
        n = int(input("¿Cuántos productos registra la guía? "))
    except ValueError:
        print("Número no válido, asumiendo 0 productos.")
        n = 0

    for _ in range(n):
        prod = input("  • Nombre del producto: ").strip()
        try:
            cantidad = int(input(f"  • Cantidad recibida de {prod}: "))
        except ValueError:
            print("  Cantidad no válida, asumiendo 0.")
            cantidad = 0

        stock[prod] = stock.get(prod, 0) + cantidad
        print(f"  → Stock de {prod}: {stock[prod]} unidades")

def registrar_rechazo(guia, motivo):
   
    rechazos.append({'guia': guia, 'motivo': motivo})
    print(f"\nRechazo registrado para la guía {guia}: {motivo}")

def recepcion_de_productos():
    
    guia_remision = input("Ingrese la guía de remisión: ").strip()
    productos_coinciden = input(
        "¿Los productos coinciden con la guía de remisión? (SI/NO): "
    ).strip().upper()

    if productos_coinciden == "SI":
        print("\n=== Recepcionando productos ===")
        update_stock(guia_remision)
        print("\nGuía firmada")
    else:
        print("\n=== Rechazando productos ===")
        motivo = input("Registrar motivo de rechazo: ").strip()
        registrar_rechazo(guia_remision, motivo)

    # Resumen final
    print("\n=== Resumen de la sesión ===")
    print("Stock final:")
    if stock:
        for prod, qty in stock.items():
            print(f" - {prod}: {qty} unidades")
    else:
        print(" - No se ha registrado ningún producto.")

    print("\nRechazos registrados:")
    if rechazos:
        for r in rechazos:
            print(f" - Guía {r['guia']}: {r['motivo']}")
    else:
        print(" - Ninguno")

if __name__ == "__main__":
    recepcion_de_productos()