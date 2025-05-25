reactivos_solicitados = []

def solicitud_de_producto():
    global reactivos_solicitados

    opcion = input('Realizara una solicitud de producto? (si/no) -> ').lower()
    
    while opcion:
        if opcion == 'no':
            print('\nDebes ingresa si o no')

            opcion = input('\nRealizara una solicitud de producto? (si/no) -> ').lower()

        else:
            descripcion = input('\nIngresa el nombre del reactivo que solicitaras: ')
            cantidad = int(input('\nIngresa la cantidad que solicitaras: '))

            while cantidad < 1:
                print('La cantidad debe ser mayor a 1 \n')
                cantidad = int(input('Ingresa la cantidad que solicitaras: '))

            reactivo = [ descripcion, cantidad ]

            reactivos_solicitados.append(reactivo)

            opcion = input('\nSeguiras ingresando productos? (si/no) -> ').lower()


    for i in range(0, len(reactivos_solicitados)):
        print(f'\n\nSolicitud N° {i + 1}')
        print('-------------')
        print('Reactivo: ', reactivos_solicitados[i][0])
        print('Cantidad: ', reactivos_solicitados[i][1], 'caj.\n')


if __name__ == '__main__':
    solicitud_de_producto()