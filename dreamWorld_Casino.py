#Segundo avance Diego Aguero
#Dreamworld casino
import getpass

id = ""
pin = ""
usuario = ""
review = 0
intentos = 0
validado = 0
dineroDisponible = 0
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
def validarUsuario():
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
                    validado = 1
                    break
        else:             
            print("Se excedió en el maximo de intentos para ingresar su PIN, volviendo al menú principal")
            #Se llama a la funcion Validar Usuarios para efectos practicos, en el main se debe llamar al menu inicial
            validarUsuario(listaUsuarios, listaPassword)     
    print("review", review)
    review = review - 1
    return usuario, review, validado


#Esta funcion realiza la revision de saldo del usuario
def revisarSaldo():
    #Para realizarlo vamos a llamar a la funcion que separa en listas las bases de datos
    #y devuelve el index del que se quiere buscar para obtener el dinero en especifico
    #listaUsuarios, listaPassword, listaDinero= separarLista()
    dineroDisponible = listaDinero[review]
    print("Dinero disponible", dineroDisponible)
    return dineroDisponible

def retirarDinero():
    dineroDisponible  = int(revisarSaldo())
    count = 1
    print("review2", review)
    r=0
    intentos = 0
    archivo = open("usuariosPrueba.txt", "w")
    archivo.truncate(0)
    archivo.close()
    #listaUsuarios, listaPassword, listaDinero= separarLista()
    print("Ingrese la cantidad de Dinero a retirar, recuerde que tiene 3 intentos para realizar el retiro")
    while intentos < 3: 
        if(count <= 3):
            #la variable count nos ayuda a saber cuantas veces se ha intentado ingresar el usuario
            count = count + 1 
            #print ("Intento #", count - 1)
            try:
                retiro = int(input("Cantidad de Dinero a retirar"))
                #print("retiro", retiro)
                #print("disponible", dineroDisponible)
                if(retiro <= dineroDisponible):
                    listaDinero[review] = int(listaDinero[review]) - retiro
                    #Agregar escritura de datos
                    with open("usuariosPrueba.txt", "w") as archivo:
                        for i in listaUsuarios:
                            archivo.write(str([listaUsuarios[r], listaPassword[r], listaDinero[r]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                            archivo.write("\n")
                            r = r + 1
                    print("El dinero retirado es de:", retiro)
                    print("El disponible actual es de:", listaDinero[review])
                    archivo.close()
                    intentos = 3
                    subMenu(usuario)
                    
                else:
                    print("El valor ingresado es mayor al disponible de la cuenta, hemos evitado la transacción")
            except ValueError:
                print("Intentelo de nuevo")
                count = count + 1
        else:
            print("Se excedió del numero de intentos")
            with open("usuariosPrueba.txt", "w") as archivo:
                for i in listaUsuarios:
                    archivo.write(str([listaUsuarios[r], listaPassword[r], listaDinero[r]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                    archivo.write(" \n")
                    r = r + 1
            subMenu(usuario)
            break
                
def depositarDinero():
    listaDivisa = []
    listaValor = []
    deposito = 0
    numeroLinea = 0
    count = 0
    valorDivisa = 0
    write = 0
    print("Las divisas soportadas son las siguientes:")
    print("1-Colones")
    print("2-Dolares")
    print("3-Bitcoin")
    with open("divisas.txt", "r") as archivo:
        for line in archivo:
            numeroLinea = numeroLinea + 1    
            line.rstrip()
            separado = line.split(" ")
            listaDivisa.append(separado[0])
            listaValor.append(separado[1])
            print(f"El valor de las divisa {listaDivisa[count]} es de {listaValor[count]}")
            count = count +1 
    archivo.close()
    count=0
    #Se realiza un try y except para tomar en cuenta que un usuario ingrese un valor distinto a los solicitados en el menu
    
        #Si el valor ingresado es 1 se llama a la funcion retirar dinero y asi consecutivamente de acuerdo a lo solicitado
    while count < 3:
        try:
            decision = int(input("En que divisa desea realizar el deposito"))
            if decision == 1:
                    #deposito = input(float("Digite la cantidad de colones para depositar"))
                    #Al momento de la revision dos se encuentra en proceso la funcion retirar dinero
                try:
                    deposito = float(input("Digite la cantidad de Colones para depositar"))
                    for i in listaDivisa:
                        if(i == "colones"):
                            valorDivisa = int(listaValor[0])
                            print(valorDivisa)
                            deposito = deposito / valorDivisa
                            print(f"El deposito en dolares a realizar es de {deposito}")
                            deposito = deposito + float(listaDinero[review])
                            deposito = round(deposito, 3)
                            print("Saldo Actual", deposito)
                            listaDinero[review] = str(deposito)
                            with open("usuariosPrueba.txt", "w") as archivo:
                                for i in listaUsuarios:
                                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                                    archivo.write("\n")
                                    write = write + 1
                    break
                except ValueError:
                    count = count +1     
                
            
            
            elif decision == 2:
                try:
                    deposito = float(input("Digite la cantidad de Dolares para depositar"))
                        #Al momento de la revision dos se encuentra en proceso la funcion de depositar dinero
                    print(f"El deposito en dolares a realizar es de {deposito}")
                    deposito = deposito + float(listaDinero[review])
                    deposito = round(deposito, 3)
                    print("Saldo Actual", deposito)
                    listaDinero[review] = str(deposito)
                    with open("usuariosPrueba.txt", "w") as archivo:
                        for i in listaUsuarios:
                            archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                            archivo.write("\n")
                            write = write + 1
                    break
                except:
                    count = count +1
                    
            
            
            elif decision == 3:
                try:
                    deposito = float(input("Digite la cantidad de Bitcoin para depositar"))
                    for i in listaDivisa:
                        if(i == "bitcoin"):
                            valorDivisa = int(listaValor[1])
                            deposito = deposito * valorDivisa
                            print(f"El deposito en dolares a realizar es de {deposito}")
                            deposito = deposito + float(listaDinero[review])
                            deposito = round(deposito, 3)
                            print("Saldo Actual", deposito)
                            listaDinero[review] = str(deposito)
                            with open("usuariosPrueba.txt", "w") as archivo:
                                for i in listaUsuarios:
                                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                                    archivo.write("\n")
                                    write = write + 1
                    break

                except ValueError:
                            #la funcion revisar saldo se encuentra corriendo
                    count = count +1
                    #print("test3")
            else:
                print("Elvalor ingresado no esta dentro de las opciones, intente de nuevo")
        except ValueError:
            count = count +1
            print("El valor ingresado no se encuentra dentro de las opciones, intentelo de nuevo")
    else:
        print("Excedio el maximo de intentos para realizar el deposito, volviendo al menu principal")
        subMenu(usuario)        


def eliminarUsuario():
    write = 0
    print("Antes de eliminar el usuario vamos a verificar su identidad")
    usuario, review, validado = validarUsuario()
    dineroDisponible = int(revisarSaldo())
    print(dineroDisponible)
    if(validado == 1):
        if dineroDisponible == 0:
            #print("aqui")
            listaUsuarios.pop(review)
            listaPassword.pop(review)
            listaDinero.pop(review)
            print(listaUsuarios)
            print(listaPassword)
            print(listaDinero)
            with open("usuariosPrueba.txt", "w") as archivo:
                for i in listaUsuarios:
                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                    archivo.write("\n")
                    write = write + 1
        else:
            print("Para eliminar el usuario debe retirar todo el dinero o volver a jugar")
            print("Regresando al menu")
            subMenu(usuario)
    else:
        print("Usuario no validado")
        print("Regresando al menu")
        subMenu(usuario)

def salir():
    #Debe salir al menu principal, regresando a submenu por temas practicos
    print("Saliendo")
    
#La funcion submenu es la principal funcion que se va a mostrar al usuario
#actualmente algunas de sus funciones se encuentran en proceso
def subMenu(usuario):
    #separarLista()
    while True:
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
                retirarDinero()
            elif decision == 2:
                #Al momento de la revision dos se encuentra en proceso la funcion de depositar dinero
                depositarDinero()
            elif decision == 3:
                #la funcion revisar saldo se encuentra corriendo
                revisarSaldo()
            elif decision == 4:
                #Se encuentra en proceso en conjunto con otro companero
                print("Juegos en linea")
            elif decision == 5:
                #Se encuentra en proceso en conjunto con otro companero
                eliminarUsuario()
            elif decision == 6:
                salir()
                
            else:
                print("Gracias por preferirnos")
        #En caso de mostrar error se cierra el programa
        except ValueError:
            print("El valor ingresado no se encuentra dentro de las opciones")



#Todavia no se ha realizado un main ya que las funciones se prueban separadas primero y se debuggean
#cuando ya funcionan se hace una revision de como trabajan en conjunto

listaUsuarios, listaPassword, listaDinero = separarLista()
usuario, review, validado = validarUsuario ()
subMenu(usuario)