#Pagina Principal dwl casino
#Autor Iganacio Toval 
#Fecha: 24/06/2023
#Funcion de la pagina pricipal y seleccion de las diferentes opcines

listaUsuarios = []
listaPassword = []
listaDinero = []
usuario = ""
review = 0
validado = 0


def mostrarPaginaPrincipal():
    print("Bienvenido a DreamWorld Casino")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")


opcion = 0  
#Ciclo para que el ussuario eliga la opcion que quiere.
while opcion != 4:
    mostrarPaginaPrincipal()
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))
    except ValueError:
        print("Error: Ingrese un número válido.")

    if opcion == 1:
        print("Ha seleccionado Registro de usuario nuevo")
        from Registro_de_Usuario import registroUsuario

    elif opcion == 2:
        from dreamWorld_Casino import Inicio

    elif opcion == 3:
        print("Ha seleccionado Configuración Avanzada")
        from Configuraón_Avanzada import mostrarMenu

    elif opcion == 4:
        print("Ha seleccionado Salir")

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")




