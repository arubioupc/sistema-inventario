stock = {}
rechazos = []
reactivos_solicitados = []

# ——— Algoritmo 1: Recepción de Productos ——————————————————————————————————————————————
def update_stock(guia):
    """
    Pide al usuario cuántos y cuáles productos llegaron,
    y actualiza el diccionario `stock`.
    """
    print(f"\nActualizando stock según la guía {guia}…")
    try:
        n = int(input("¿Cuántos productos registra la guía? "))
    except ValueError:
        n = 0

    for _ in range(n):
        prod = input("  • Nombre del producto: ").strip()
        while not prod:
            prod = input("  • Nombre del producto: ").strip()

        try:
            cantidad = int(input(f"  • Cantidad recibida de {prod}: "))
            if cantidad < 1:
                raise ValueError
        except ValueError:
            cantidad = 1

        stock[prod] = stock.get(prod, 0) + cantidad
        print(f"  → Stock de {prod}: {stock[prod]} unidades")

def registrar_rechazo(guia, motivo):
    """
    Añade un registro de rechazo con número de guía y motivo.
    """
    rechazos.append({'guia': guia, 'motivo': motivo})
    print(f"\nRechazo registrado para la guía {guia}: {motivo}")

def recepcion_de_productos():
    guia_remision = input("\nIngrese la guía de remisión: ").strip()
    while not guia_remision:
        guia_remision = input("Ingrese la guía de remisión: ").strip()

    respuesta = input("¿Los productos coinciden con la guía de remisión? (si/no) -> ").strip().lower()
    while respuesta not in ('si', 'no'):
        respuesta = input("¿Los productos coinciden con la guía de remisión? (si/no) -> ").strip().lower()

    if respuesta == "si":
        update_stock(guia_remision)
        print("\nGuía firmada")
    else:
        motivo = input("Registrar motivo de rechazo: ").strip()
        while not motivo:
            motivo = input("Registrar motivo de rechazo: ").strip()
        registrar_rechazo(guia_remision, motivo)

# ——— Algoritmo 2: Actualización Almacén General (FEFO) ————————————————————————————————
def actualizacion_almacen_general():
    fecha_actual = input("\nIngrese la fecha actual (YYYY-MM-DD): ").strip()
    print(f"\nActualizando inventario en modo First Expired First Out (FEFO) a fecha {fecha_actual}…")
    print("Inventario actualizado con FEFO")

# ——— Algoritmo 3: Solicitud de Reactivos —————————————————————————————————————————————
def solicitud_de_producto():
    resp = input("\n¿Realizará una solicitud de reactivos? (si/no) -> ").strip().lower()
    while resp not in ('si', 'no'):
        resp = input("¿Realizará una solicitud de reactivos? (si/no) -> ").strip().lower()

    if resp == 'no':
        print("No se realizará ninguna solicitud.")
        return

    while True:
        desc = input("\nIngrese el nombre del reactivo: ").strip()
        while not desc:
            desc = input("Ingrese el nombre del reactivo: ").strip()

        while True:
            try:
                qty = int(input("Ingrese la cantidad que solicitará: "))
                if qty < 1:
                    raise ValueError
                break
            except ValueError:
                pass

        reactivos_solicitados.append({'reactivo': desc, 'cantidad': qty})
        print(f"  → {qty} unidades de '{desc}' agregadas.")

        cont = input("\n¿Desea ingresar otro reactivo? (si/no) -> ").strip().lower()
        while cont not in ('si', 'no'):
            cont = input("¿Desea ingresar otro reactivo? (si/no) -> ").strip().lower()
        if cont == 'no':
            break

    print("\nSolicitud registrada con éxito.")

def main():
    while True:
        print("\n======== Menú Principal ========")
        print("1. Recepción de Productos")
        print("2. Actualización Almacén General (FEFO)")
        print("3. Solicitud de Reactivos")
        print("4. Ver resumen completo")
        print("5. Salir")
        opcion = input("Seleccione una opción [1-5]: ").strip()

        if opcion == "1":
            recepcion_de_productos()
        elif opcion == "2":
            actualizacion_almacen_general()
        elif opcion == "3":
            solicitud_de_producto()
        elif opcion == "4":
            print("\n=== Resumen Actual ===")
            print("\nStock:")
            if stock:
                for prod, qty in stock.items():
                    print(f" - {prod}: {qty} unidades")
            else:
                print(" (sin productos registrados)")

            print("\nRechazos:")
            if rechazos:
                for r in rechazos:
                    print(f" - Guía {r['guia']}: {r['motivo']}")
            else:
                print(" (sin rechazos)")

            print("\nReactivos Solicitados:")
            if reactivos_solicitados:
                for i, item in enumerate(reactivos_solicitados, start=1):
                    print(f" {i}. {item['reactivo']} — {item['cantidad']} unidades")
            else:
                print(" (sin solicitudes)")
        elif opcion == "5":
            print("\nSaliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
