#importar getpass para que no se va la contraaseña
import getpass

#Binvenida al resgistro de ususario
print("Bienvenido al registro de usuario")


# variables de las diferentes monedas y sus comverciones.
valorMinimo = 200
dolares = 1
colones = 536
bitcoin = 30590  # Tasa de cambio ficticia del Bitcoin a dólares (1 Bitcoin = 30590 dólares)
colonesADolares = 0.0018  # Tasa de cambio ficticia de Colones a dólares (1 Colón = 0.0018 dólares)

#Funcion de ingreso e datos.
def registroUsuario():
    intentos = 0

#bucle para el registro de usuario, contraseña y deposito.
    while intentos < 3:

        #pedirle al ususario un nick.
        usuarioNuevo = input("Ingrese su usuario: ")

#Pedir nombre al ususario
        if usuarioNuevo.isalnum() and len(usuarioNuevo) >= 5:
            nombre = input("Ingrese su nombre: ")
            
#pidir el pin, ussuan el getpass.            
            while True:
                pinNuevo = getpass.getpass("Ingrese su pin: ")
                if len(pinNuevo) >= 6 and pinNuevo.isdigit():
                    print("Su pin es correcto")
                    
                    
                    depositoMinimo = valorMinimo
                    
                    intentosDeposito = 0
                    #Bucle para el deposto.                   
                    while intentosDeposito < 3:
                        deposito = int(input("Ingrese su depósito: "))
                        
                        #Pedir el tipo de moneda que desea ingresar el ususario
                        moneda = input("Ingrese su moneda (dolares, colones o bitcoin): ")
                        
                        # Identificar el tipo de moneda.                      
                        if moneda == "dolares":    
                            if deposito >= valorMinimo:
                                print(f"Depósito en dólares correcto: {deposito}")
                                break
                            else:
                                print("Ingrese un monto correcto")
                        elif moneda == "colones":
                            montoEnDolares = deposito * colonesADolares  # Convertir el monto a dólares
                            if montoEnDolares >= valorMinimo:
                                print(f"Depósito en colones correcto: {deposito} (equivalente en dólares: {montoEnDolares:.2f})")
                                break
                            else:
                                print("Ingrese un monto correcto")
                        elif moneda == "bitcoin":
                            montoEnDolares = deposito * bitcoin  # Convertir el monto a dólares
                            if montoEnDolares >= valorMinimo:
                                print(f"Depósito en Bitcoin correcto: {deposito} (equivalente en dólares: {montoEnDolares:.2f})")
                                break
                            else:
                                print("Ingrese un monto correcto")
                        else:
                            print("Moneda no válida. Intente nuevamente.")
<<<<<<< Updated upstream
                    
                    else:
                        print("Has excedido los intentos de depósito.")
                        return
                    
                    print("Usuario Ingresado")
=======
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
                        archivo.write(f"ID {usuarioNuevo} \nNombre {nombre} \nContrasena {pinNuevo} \nDeposito {monto:.2f} ")

                    # Mostrar mensaje de registro exitoso y regresar True para indicar éxito
>>>>>>> Stashed changes
                    print("¡Registro Exitoso!")
                    print("Bienvenido a DreamWorld Casino")
                    return usuarioNuevo
                else:
                    print("¡Inténtelo de nuevo!")
            #darle la binvenido al usuario.
            print("Usuario Ingresado")
            print("¡Registro Exitoso!")
            print("Bienvenido a DreamWorld Casino")
            return usuarioNuevo
        else:
            print("Ingrese un usuario alfanumérico de al menos 5 caracteres")
            intentos += 1
    #Advertencia de exeso de intento y regreessar al menu principal
    print("Has excedido todos los intentos. Regresando al menú principal")
    return None
#Almacenar los ussuarios registrados
usuariosRegistrados = []

#Bule de registro de usuario.
while True:
    usuarioNuevo = registroUsuario()
    
    if usuarioNuevo is not None:
        usuariosRegistrados.append(usuarioNuevo)
        print("Su Usuario es: ")
        for usuarioNuevo in usuariosRegistrados:
            print(usuarioNuevo)
        break

