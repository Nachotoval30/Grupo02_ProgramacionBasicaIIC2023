import getpass
import os

# Bienvenida al registro de usuario
print("Bienvenido al registro de usuario")

# Variables de las diferentes monedas y sus conversiones.
valorMinimo = 200
dolares = 1
colones = 536
bitcoin = 30590
colonesADolares = 0.0018

# Carpeta principal donde se guardarán los usuarios y archivos.
carpetaUsuarios = "usuarios"

# Crear la carpeta de usuarios si no existe
if not os.path.exists(carpetaUsuarios):
    os.mkdir(carpetaUsuarios)

# Función para verificar si el usuario ya está registrado
def usuarioExiste(usuario):
    rutaCarpetaUsuario = os.path.join(carpetaUsuarios, usuario)
    return os.path.exists(rutaCarpetaUsuario)

# Función para el registro de usuario, contraseña y depósito.
def registroUsuario():
    intentosRegistro = 0

    while intentosRegistro < 3:
        usuarioNuevo = input("Ingrese su usuario: ")

        if usuarioNuevo.isalnum() and len(usuarioNuevo) >= 5:
            if usuarioExiste(usuarioNuevo):
                print("El usuario ya está registrado. Intente con otro nombre de usuario.")
                intentosRegistro += 1
                if intentosRegistro >= 3:
                    print("Se excedió el máximo de intentos para ingresar un ID válido, volviendo al menú principal.")
                    return False
                continue  # Solicitar un nuevo nombre de usuario si el actual ya está registrado

            nombre = input("Ingrese su nombre: ")

            while True:
                pinNuevo = getpass.getpass("Ingrese su pin: ")
                if len(pinNuevo) >= 6 and pinNuevo.isdigit():
                    print("Su pin es correcto")

                    # Proceso de depósito obligatorio
                    while True:
                        print("Monedas disponibles para depósito: dólares, colones, bitcoin")
                        moneda = input("Ingrese la moneda de su depósito: ").lower()

                        if moneda == "dólares":
                            monto = float(input("Ingrese el monto en dólares: "))
                        elif moneda == "colones":
                            monto = float(input("Ingrese el monto en colones: "))
                            monto = monto * colonesADolares
                        elif moneda == "bitcoin":
                            monto = float(input("Ingrese el monto en bitcoin: "))
                            monto = monto * bitcoin
                        else:
                            print("Moneda no válida. Intente nuevamente.")
                            continue

                        if monto >= valorMinimo:
                            break
                        else:
                            print("El depósito mínimo es de $200. Intente nuevamente.")

                    # Crear una carpeta para el nuevo usuario
                    rutaCarpetaUsuario = os.path.join(carpetaUsuarios, usuarioNuevo)
                    if not os.path.exists(rutaCarpetaUsuario):
                        os.mkdir(rutaCarpetaUsuario)

                    # Guardar la información del usuario en un archivo
                    rutaArchivoUsuario = os.path.join(rutaCarpetaUsuario, "informacionUsuario.txt")
                    with open(rutaArchivoUsuario, "w") as archivo:
                        archivo.write(f"ID {usuarioNuevo} \nNombre {nombre} \nContrasena {pinNuevo} \nDepósito {monto:.2f} ")

                    # Mostrar mensaje de registro exitoso y regresar True para indicar éxito
                    print("¡Registro Exitoso!")
                    print("Bienvenido a DreamWorld Casino")
                    return True
                else:
                    print("¡Inténtelo de nuevo!")

            
        else:
            print("Ingrese un usuario alfanumérico de al menos 5 caracteres")
            intentosRegistro += 1

    print("Se excedió el máximo de intentos para ingresar un ID válido, volviendo al menú principal.")
    return False

# Bucle de registro de usuario.
while True:
    registrado = registroUsuario()

    if registrado:
        break

