#Segundo avance Diego Aguero
#Dreamworld casino
import getpass

id = ""
pin = ""
usuario = ""
review = 0
intentos = 0
listaUsuarios = []
listaPassword = []
listaDinero = []

#En la siguiente funcion separamos el archivo en diferentes listas, para asi tener los usuarios, password y dineros registrados
#Tomar en cuenta que el archivo al que llama es una prueba
def separarLista():
    numeroLinea = 0
    #Con el archivo abierto el programa hara una revision de toda la lista y hara un append de las listas dependiendo de si es usuario, password o dinero
    #Tomar en cuenta que en el archivo se tiene que tener el formato 
    #Usuario Password Dinero
    with open("usuariosPrueba.txt", "r") as archivo:
        for line in archivo:
            numeroLinea = numeroLinea + 1
            line.rstrip()
            separado = line.split(" ")
            listaUsuarios.append(separado[0])
            listaPassword.append(separado[1])
            listaDinero.append(separado[2])
    print(listaUsuarios)
    print(listaPassword)
    print(listaDinero)
    #Se tiene que cerrar el archivo antes de terminar la funcion para poder usarse despues y no desperdiciar memoria
    archivo.close()
    return listaUsuarios, listaPassword, listaDinero

#En esta funcion validamos el usuario junto con su password
def validarUsuario(listaUsuarios, listaPassword):
    intentos = 0
    count = 1
    review = 0
    #Recordamos en el primer print al usuario que solo cuenta con 3 intentos
    print("Ingrese el usuario solicitado, recuerde que solo tiene 3 intentos")
    while intentos < 3:
        if(count <= 3):
            #la variable count nos ayuda a saber cuantas veces se ha intentado ingresar el usuario
            count = count + 1 
            print ("Intento #", count - 1)
            id = getpass.getpass("Ingrese el ID de usuario:")
            review = 0
            #El for hace una revision de la lista de usuarios para saber si el mismo hace match con los que se encuentran en la base de datos
            for usuario in listaUsuarios:
                #La variable review funciona para llevar el conteo de las veces que se revisa la lista hasta que se encuentre un match
                #esto nos va a servir cuando se quiera validar el password del cliente
                review = review + 1
                print("index", review)
                if(id == usuario):
                    intentos = 3
                    print("index", review)
                    print("id", id)
                    print("Usuario ingresado correctamente")
                    break
        else:             
            print("Se excedió en el maximo de intentos para ingresar su ID, volviendo al menú principal")
            #Se llama a la funcion Validar Usuarios para efectos practicos, en el programa final se va a llamar al menu inicial
            validarUsuario(listaUsuarios, listaPassword)    

    #La siguiente seccion trabaja de la misma manera que la anterior con un pequeno cambio
    count = 1
    intentos = 0
    print("Ingrese el PIN solicitado, recuerde que solo tiene 3 intentos")
    while intentos < 3:
        if(count <= 3):
            count = count + 1 
            print ("Intento #", count - 1)
            PIN = getpass.getpass("Ingrese el PIN de usuario:")
            for password in listaPassword:
                #Cuando el cliente ingrese su contrasena, vamos a revisar la lista de contrasenas, con el indice en especifico de la variable
                #review para que haga match con la ingresada por el usuario
                if(PIN == listaPassword[review - 1]):
                    intentos = 3
                    print("PIN", PIN)
                    print("PIN ingresado correctamente")
                    break
        else:             
            print("Se excedió en el maximo de intentos para ingresar su PIN, volviendo al menú principal")
            #Se llama a la funcion Validar Usuarios para efectos practicos, en el main se debe llamar al menu inicial
            validarUsuario(listaUsuarios, listaPassword)     
    return usuario, review

#Esta funcion realiza la revision de saldo del usuario
def revisarSaldo(usuario):
    #Para realizarlo vamos a llamar a la funcion que separa en listas las bases de datos
    #y devuelve el index del que se quiere buscar para obtener el dinero en especifico
    separarLista()
    dineroDisponible = listaDinero[review]
    print("Dinero disponible", dineroDisponible)

#La funcion submenu es la principal funcion que se va a mostrar al usuario
#actualmente algunas de sus funciones se encuentran en proceso
def subMenu(usuario):
    intentos = 0
    print("Bienvenido a dreamworld casino ", usuario)
    print("Para retirar dinero digite 1")
    print("Para depositar dinero digite 2")
    print("Para revisar su saldo actual digite 3")
    print("Para jugar en linea digite 4")
    print("Para eliminar su usuario digite 5")
    print("Para salir digite 6")
    #Se realiza un try y except para tomar en cuenta que un usuario ingrese un valor distinto a los solicitados en el menu
    try:
        decision = int(input("Seleccione una opción"))
        #Si el valor ingresado es 1 se llama a la funcion retirar dinero y asi consecutivamente de acuerdo a lo solicitado
        
        if decision == 1:
            #Al momento de la revision dos se encuentra en proceso la funcion retirar dinero
            print("Retirar dinero")
        elif decision == 2:
            #Al momento de la revision dos se encuentra en proceso la funcion de depositar dinero
            print("Depositar dinero")
        elif decision == 3:
            #la funcion revisar saldo se encuentra corriendo
            print("Revisar saldo")
        elif decision == 4:
            #Se encuentra en proceso en conjunto con otro companero
            print("Juegos en linea")
        elif decision == 5:
            #Se encuentra en proceso en conjunto con otro companero
            print("Eliminar usuario")
        elif decision == 6:
            print("Salir")
        else:
            print("Gracias por preferirnos")
    #en caso de mostrar error se cierra el programa
    except ValueError:
        print("El valor ingresado no se encuentra dentro de las opciones")

#Todavia no se ha realizado un main ya que las funciones se prueban separadas primero y se debuggean
#cuando ya funcionan se hace una revision de como trabajan en conjunto
separarLista()
validarUsuario(listaUsuarios, listaPassword)
revisarSaldo(review)
subMenu(usuario)