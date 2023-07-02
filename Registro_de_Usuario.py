#Creacion de nombre de ususraio
import getpass
print("Bienvenido al resgistro de ususario")
valor_minimo = 200
dolares = 1
colones = 536
bitcoin = 30590
deposto_usuario = list[] 
def registro_usuario():
    intentos = 0
   
    while intentos < 3:
        usuario_nuevo = input("Ingrese su usuario: ")
        
        if usuario_nuevo.isalnum() and len(usuario_nuevo) >= 5:
            nombre = input("Ingrese su nombre: ")
            while True:
                pin_nuevo = getpass.getpass("Ingrese su pin: ")
                if len(pin_nuevo) >= 6 and pin_nuevo.isdigit():
                    print("Su pin es correcto")
                    deposito_minimo = valor_minimo()
                    intentos_deposito = 0
                    while intentos_deposito < 3:
                        deposito = input("Ingrese su deposito: ")
                        moneda = input("Ingrese su moneda: ")
                        if  moneda == dolares:    
                            if deposito >= valor_minimo:
                                print(f"Deposito correcto: ",{deposito})
                                break
                            else:
                                print("Ingrese un monto correcto")
                        elif moneda ==  colones:




                    break
                else:
                    print("¡Intntelo de nuevo!")
            print("Usuario Ingresado")
            print("¡Registro Exitoso!")
            print("Bienvendo a DreamWorld Casino")
            return usuario_nuevo
        else:
            print("Ingrese un usuario Alphanumerico y de 5 caracteres")
            intentos += 1
    
    print("Has exedido todo los intentos, \n Regresando al menú principal")

usuarios_registrados = set()

while True:
    usuario_nuevo = registro_usuario()
    if usuario_nuevo in usuarios_registrados:
        print("El ususario ya existe, Ingrese otro.")
    else:
        usuarios_registrados.add(usuario_nuevo)
        print("Su Usuario es: ")
    for usuario_nuevo in usuarios_registrados:
        print(usuario_nuevo)


registro_ususario()

