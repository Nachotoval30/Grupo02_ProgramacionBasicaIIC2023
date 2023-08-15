#importamos el getpass para el pin especial.
#importamos el os para el manejo de carpetas.

import getpass
import os
import shutil
#Función para solicitar el pin especial.
def solicitarPIN():
    pinEspecial = "1234"  # Define aquí el PIN especial según las especificaciones
    intentos = 3
    while intentos > 0:
        inputPin = getpass.getpass("Ingrese el PIN especial: ")
        if inputPin == pinEspecial:
            return True
        else:
            intentos -= 1
            print(f"PIN incorrecto. Le quedan {intentos} intentos.")
    return False

#Función para eliminar el resgitro de un ususario.
def eliminarUsuario(carpetaUsuario):
    try:
        shutil.rmtree(carpetaUsuario)
        print("El registro fue eliminado con éxito.\n")
    except FileNotFoundError:
        print("No se encontró ningún registro que coincida con su nombre.")
    except Exception as e:
        print(f"No se pudo eliminar el archivo '{carpetaUsuario}': {str(e)}")

#Funcion que muestra el mei principal de la configuración avanzada 
def mostrarMenu():
    print("Seleccione la opción que desea realizar:")
    print("1. Eliminar Usuario")
    print("2. Configuraciones Avanzadas")
    print("3. Salir")

#Ciclo para selelcion la opcion.
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción deseada: "))
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

        if opcion == 1:
            print("Ha seleccionado eliminar usuario.")
            usuarioAEliminar = input("Ingrese el ID del usuario que desea eliminar: ")
            rutaCarpetaUsuarioAEliminar = os.path.join("usuarios", usuarioAEliminar)  # Reemplaza esto con la ruta correcta
            eliminarUsuario(rutaCarpetaUsuarioAEliminar)
        
        elif opcion == 2:
            print("Ha seleccionado configuraciones avanzadas.")
            mostrarMenuModificacion()
            break
        elif opcion == 3:
            print("Regresando al menú principal.")
            break
        else:
            print("Opción inválida, ingrese una opción existente.")
            continue

#Funcion para crear la carpeta de los valores del sistema.
def crearArchivoConfiguracion():
    archivo = open("configuracionAvanzada.txt", "w")
    archivo.write("545\n")
    archivo.write("29000\n")
    archivo.write("30000\n")
    archivo.write("50\n")
    archivo.write("50\n")
    archivo.write("200\n")
    archivo.close()

#Función para cambiar los valores del sistema
def modificarValorConfiguracion(opcion):
    archivo = open("configuracionAvanzada.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    valor_actual = lineas[opcion - 1].strip()
    nuevo_valor = input(f"Ingrese el nuevo valor para la opción {opcion}: ")
    lineas[opcion - 1] = f"{nuevo_valor}\n"

    archivo = open("configuracionAvanzada.txt", "w")
    archivo.writelines(lineas)
    archivo.close()

#Función para seleccionar el valor que desea cambiar.
def mostrarMenuModificacion():
    print("Seleccione la opción que desea modificar:")
    print("1. Tipo de cambio: Compra de dólares usando colones")
    print("2. Tipo de cambio: Compra de dólares usando bitcoins")
    print("3. Valor acumulado Tragamonedas")
    print("4. Apuesta mínima Tragamonedas")
    print("5. Apuesta mínima Blackjack")
    print("6. Inversión mínima para registrarse")
    print("7. Regresar al menú principal")

#Ciclo para selecionar la opccion.
    while True:
        try:
            opcionModificacion = int(input("Ingrese el número de la opción deseada: "))
            if opcionModificacion == 7:
                print("Regresando al menú principal.")
                break
            elif 1 <= opcionModificacion <= 6:
                modificarValorConfiguracion(opcionModificacion)
                print("Valor modificado exitosamente.")
            else:
                print("Opción inválida, ingrese una opción existente.")
                continue
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

if solicitarPIN():
    mostrarMenu()


