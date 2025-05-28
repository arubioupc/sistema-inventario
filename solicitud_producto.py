reactivos_solicitados = []

def solicitud_de_producto():
    
    while True:
        opcion = input('¿Realizará una solicitud de producto? (si/no) -> ').strip().lower()
        if opcion in ('si', 'no'):
            break
        print("Por favor, responda 'si' o 'no'.")
    
    if opcion == 'no':
        print("\nNo se realizará ninguna solicitud.")
        return  

    
    while True:
        
        descripcion = input('\nIngresa el nombre del reactivo que solicitarás: ').strip()
        while not descripcion:
            print("La descripción no puede estar vacía.")
            descripcion = input('Ingresa el nombre del reactivo que solicitarás: ').strip()
        
        
        while True:
            try:
                cantidad = int(input('Ingresa la cantidad que solicitarás: '))
                if cantidad < 1:
                    print("La cantidad debe ser un número entero positivo.")
                    continue
                break
            except ValueError:
                print("Cantidad no válida. Debe ingresar un número entero.")

        
        reactivos_solicitados.append([descripcion, cantidad])

        
        while True:
            opcion = input('\n¿Seguirás ingresando productos? (si/no) -> ').strip().lower()
            if opcion in ('si', 'no'):
                break
            print("Por favor, responda 'si' o 'no'.")

        if opcion == 'no':
            break  

   
    print("\n=== Resumen de la solicitud ===")
    for i, (prod, qty) in enumerate(reactivos_solicitados, start=1):
        print(f"\nSolicitud N° {i}")
        print("-------------")
        print(f"Reactivo: {prod}")
        print(f"Cantidad: {qty} caj.\n")

if __name__ == '__main__':
    solicitud_de_producto()
