#Pagina Principal dwl casino
#Autor Iganacio Toval 
#Fecha: 24/06/2023 


def mostrar_pagina_principal():
    print("Bienvenido a DreamWorld Casino")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")

opcion = 0

while opcion != 4:
    mostrar_pagina_principal()
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        print("Ha seleccionado Registro de usuario nuevo")
        # Aquí puedes agregar el código para el registro de nuevos usuarios

    elif opcion == 2:
        print("Ha seleccionado DreamWorld Casino")
        # Aquí puedes agregar el código para el casino

    elif opcion == 3:
        print("Ha seleccionado Configuración Avanzada")
        # Aquí puedes agregar el código para la configuración avanzada

    elif opcion == 4:
        print("Ha seleccionado Salir")
        # Aquí puedes agregar el código para finalizar el programa

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")