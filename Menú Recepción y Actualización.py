
stock = {}       # Diccionario para llevar el stock de cada producto.
rechazos = []    # Lista para almacenar los rechazos registrados.

# ——— Algoritmo 1: Recepción de Productos ——————————————————————————————————————————————
def update_stock(guia):
   
    print(f"\nActualizando stock según la guía {guia}…")
    try:
        n = int(input("¿Cuántos productos registra la guía? "))
    except ValueError:
        print("Número no válido. Asumiendo 0 productos.")
        n = 0

    for _ in range(n):
        prod = input("  • Nombre del producto: ").strip()
        try:
            cantidad = int(input(f"  • Cantidad recibida de {prod}: "))
        except ValueError:
            print("  Cantidad no válida. Asumiendo 0.")
            cantidad = 0

        stock[prod] = stock.get(prod, 0) + cantidad
        print(f"  → Stock de {prod}: {stock[prod]} unidades")

def registrar_rechazo(guia, motivo):
    
    rechazos.append({'guia': guia, 'motivo': motivo})
    print(f"\nRechazo registrado para la guía {guia}: {motivo}")

def recepcion_de_productos():
    
    guia_remision = input("Ingrese la guía de remisión: ").strip()
    respuesta = input("¿Los productos coinciden con la guía de remisión? (SI/NO): ")\
                .strip().upper()

    if respuesta == "SI":
        print("\n=== Recepcionando productos ===")
        update_stock(guia_remision)
        print("\nGuía firmada ")
    else:
        print("\n=== Rechazando productos ===")
        motivo = input("Registrar motivo de rechazo: ").strip()
        registrar_rechazo(guia_remision, motivo)

# ——— Algoritmo 2: Actualización Almacén General (FEFO) ————————————————————————————————
def actualizacion_almacen_general():
    
    fecha_actual = input("\nIngrese la fecha actual (YYYY-MM-DD): ").strip()
    print(f"\nActualizando inventario en modo First Expired First Out (FEFO) a fecha {fecha_actual}…")
    
    print("Inventario actualizado con FEFO")

# ——— Función principal con menú ——————————————————————————————————————————————————————
def main():
    while True:
        print("\n======== Menú de Operaciones ========")
        print("1. Recepción de Productos")
        print("2. Actualización Almacén General (FEFO)")
        print("3. Ver resumen de stock y rechazos")
        print("4. Salir")
        opcion = input("Seleccione una opción [1-4]: ").strip()

        if opcion == "1":
            recepcion_de_productos()
        elif opcion == "2":
            actualizacion_almacen_general()
        elif opcion == "3":
            # Resumen completo
            print("\n=== Resumen Actual ===")
            print("Stock:")
            if stock:
                for p, q in stock.items():
                    print(f" - {p}: {q} unidades")
            else:
                print("  (sin productos registrados)")
            print("\nRechazos:")
            if rechazos:
                for r in rechazos:
                    print(f" - Guía {r['guia']}: {r['motivo']}")
            else:
                print("  (sin rechazos)")
        elif opcion == "4":
            print("\nSaliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()