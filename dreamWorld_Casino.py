<<<<<<< Updated upstream
=======
#Segundo avance Diego Aguero
#Dreamworld casino
import getpass
import random
import sys
import time

#Estas variables se deben cargar desde la configuración avanzada
dineroJugador = 300
apuestaMinima = 200
acumulado = 0
contador = 0
apuesta = 0

#Simbolos de las cartas
figuras = ['♠', '♥', '♦', '♣']

valorFiguras = {
    "@": 1,
    "#": 2,
    "+": 3,
    "7": acumulado
}
valores = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

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
    #print(listaUsuarios)
    #print(listaPassword)
    #print(listaDinero)
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
    
####################################################
#Verificar que el jugador tenga el mínimo de dinero para poder jugar
def verificarDinero():
    dineroJugador = listaDinero[review]
    dineroJugador = float(dineroJugador)
    #print("DINERRRROOOOOO", dineroJugador)
    if dineroJugador < apuestaMinima:
        print(f"Lo sentimos, no tienes el monto mínimo para jugar. La apuesta minima es de: ${apuestaMinima}")
        #CAMBIAAAAARRRR DEBE VOLVER AL SUBMENU DE JUEGOS
        subMenu(usuario)
    else:
        print(f"Tu saldo actual es: ${dineroJugador}")
        return dineroJugador
    

def obtenerApuesta():
    global apuesta
    dineroJugador = listaDinero[review]
    dineroJugador = float(dineroJugador)
    write = 0
    #global dineroJugador
    while True:
        try:
            opcion = int(input("Para jugar presiona 1, para salir presiona 2:  "))
        except ValueError:
            print("Lo sentimos, debes ingresar un número entero.")
            continue
        if opcion == 2:
            #####Escribir el valor en el archivo
            listaDinero[review] = str(dineroJugador)
            print(f"Tu nuevo saldo actual es: ${dineroJugador}")
            with open("usuariosPrueba.txt", "w") as archivo:
                for i in listaUsuarios:
                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                    archivo.write("\n")
                    write = write + 1
                    #print("ESCRIBIENDOO")
            print("Gracias por participar.")
            sys.exit()
        elif opcion == 1:
            try:
                apuesta = int(input("Ingresa el monto de tu apuesta para jugar: "))
            except ValueError:          
                print("Lo sentimos, debes ingresar un número entero.")
                continue
            else:
                if apuesta < apuestaMinima:
                    print(f"Lo sentimos, la apuesta mínima es de: ${apuestaMinima}")
                elif apuesta > dineroJugador:
                    print(f"Lo sentimos, no tienes saldo suficiente para apostar ${apuesta}. Tu saldo actual es: ${dineroJugador}")
                else:
                    print(f"Tu nuevo saldo actual es: ${dineroJugador - apuesta}")
                    listaDinero[review] = str(dineroJugador - apuesta)
                    #print("TESTEST", listaDinero[review])
                    return apuesta, dineroJugador

####################################################

#def verificarDinero():
#    global dineroJugador
#    #Verificar si el jugador tiene el monto mínimo para jugar
#    if dineroJugador < apuestaMinima:
#        print(f"Lo sentimos, no tienes el monto mínimo para jugar. La apuesta minima es de: ${apuestaMinima}")
#        #CAMBIAAAAARRRR DEBE VOLVER AL SUBMENU DE JUEGOS
#        sys.exit()
#    else:
#        print(f"Tu saldo actual es: ${dineroJugador}")
#        return dineroJugador
    
'''def obtenerApuesta():
    global apuesta
    global dineroJugador

    #Obtener apuesta del jugador, verificar que sea un número válido y que sea mayor o igual a la apuesta mínima y menor o igual al saldo del jugador
    while True:
        try:
            apuesta = float(input("Ingresa el monto de tu apuesta para jugar: "))
        except ValueError:          
            print("Lo sentimos, debes ingresar un número entero.")
            continue
        else:
            if apuesta < apuestaMinima:
                print(f"Lo sentimos, la apuesta mínima es de: ${apuestaMinima}")
            elif apuesta > dineroJugador:
                print(f"Lo sentimos, no tienes saldo suficiente para apostar ${apuesta}. Tu saldo actual es: ${dineroJugador}")
            else:
                print(f"Tu nuevo saldo actual es: ${dineroJugador - apuesta}")
                return apuesta, dineroJugador
'''

def obtenerBaraja():
    #Obtener baraja de forma aleatoria
    baraja = []
    for figura in figuras:
        for valor in valores:
            baraja.append((valor, figura))
    random.shuffle(baraja)
    return baraja  


def repartirCartas():
    global cartasJugador
    global cartasCrupier
    global cartaJugador1
    global cartaJugador2
    global cartaCrupier1
    global cartaCrupier2

    baraja = obtenerBaraja()

    #Repartir cartas al jugador y al crupier
    cartaJugador1 = baraja.pop()
    cartaCrupier1 = baraja.pop()
    cartaJugador2 = baraja.pop()
    cartaCrupier2 = baraja.pop()

    #Asignar las cartas de cada uno
    cartasJugador = [cartaJugador1, cartaJugador2]
    cartasCrupier = [cartaCrupier1, cartaCrupier2]

    #Mostrar las cartas del jugador y del crupier, de una por una ocultando la carta 1 del crupier
    print('')
    time.sleep(1)
    print('Jugador 1: ', cartaJugador1)
    time.sleep(1)   
    print('Crupier 1: carta oculta')
    time.sleep(1)
    print('Jugador 2: ', cartaJugador2)
    time.sleep(1)
    print('Crupier 2: ', cartaCrupier2)
    time.sleep(1)
    print('')

    #Verificar si el jugador tiene dos cartas iguales, si es así, preguntar si desea dividir su jugada
    dividirJugada()
    #Se le pregunta al jugador si desea doblar su apuesta
    doblarApuesta()

    #Mostrar las cartas del jugador y del crupier, de una por una ocultando la carta 1 del crupier
    print(f'Cartas del jugador: {cartaJugador1}, {cartaJugador2}\n')
    print(f"Cartas del crupier: ('?', '?'), {cartaCrupier2}\n")

    #Preguntar si desea pedir una nueva carta o desea plantarse
    otraCarta()
    #Mostrar la carta oculta del crupier
    print(f"Cartas del crupier: {cartaCrupier1}, {cartaCrupier2}\n")    
    return cartasJugador, cartasCrupier, cartaJugador1, cartaJugador2, cartaCrupier1, cartaCrupier2


def doblarApuesta():
    global apuesta
    global dineroJugador

    #Se le pregunta al jugador si desea doblar su apuesta, si es así, se le duplica la apuesta y se le resta al saldo del jugador
    while True:
        try:
            opcion = int(input("¿Deseas doblar tu apuesta? Presiona 1 (sí), presiona 2 (no): "))
        except ValueError:
            continue
        if opcion == 1:
            if apuesta * 2 <= dineroJugador:
                apuesta = apuesta * 2
                print(f"Tu apuesta se ha duplicado. Ahora es de ${apuesta}\n")
                time.sleep(0.5)
                print(f"Tu nuevo saldo actual es: ${dineroJugador - apuesta}\n")
                time.sleep(0.5)
                return apuesta, dineroJugador
            else:
                print(f"Lo sentimos, no tienes saldo suficiente para apostar ${apuesta * 2}.")
                continue
        elif opcion == 2:
            print(f"Tu saldo actual es: ${dineroJugador - apuesta}\n")
            return apuesta, dineroJugador
        else:
            print("Lo sentimos, debes ingresar un número entero.")
            continue


def otraCarta():
    
    global cartasJugador
    global otraCartaJugador

    #Se le pregunta al usuario si desea pedir una nueva carta o desea plantarse
    while True:
        try:
            opcion = int(input("¿Deseas pedir una nueva carta? Presiona 1 (sí), presiona 2 (no): "))
        except ValueError:
            print("Lo sentimos, debes ingresar un número entero.")
            continue
        if opcion == 1:
            cartaNueva = random.choice(obtenerBaraja())
            cartasJugador.append(cartaNueva)
            time.sleep(1)
            print(f"Tu nueva carta es: {cartaNueva}")
            time.sleep(1)
            print(f"Tu nueva mano es: {cartasJugador}")
        elif opcion == 2:
            print(f"Cartas del jugador: {cartasJugador}")
            break
        else:
            print("Lo sentimos, debes ingresar un número entero.")
            continue


def asignarValorJugador():
    
    global cartasJugador
    global valorCartasJugador
    global valorTotalJugador
    valorCartasJugador = []

    #Asignar valor a la mano del jugador, tomar los valores del diccionario y sumarlos, si es 'A' preguntar si desea que valga 1 u 11
    for carta in cartasJugador:
        valorCarta = valores[carta[0]]
        valorCartasJugador.append(valorCarta)
    valorTotalJugador = sum(valorCartasJugador)
    if 1 in valorCartasJugador:
        while True:    
            try:
                opcion = int(input("¿Deseas que el As valga 1 u 11?: "))
            except ValueError:
                print("Lo sentimos, debes ingresar un número entero.")
                continue
            if opcion == 1:
                valorTotalJugador = valorTotalJugador
                break
            elif opcion == 11:
                valorTotalJugador = valorTotalJugador + 10
                break
            else:
                print("Lo sentimos, debes ingresar un número entero.")
                continue
    print(f"El valor de tu mano es: {valorTotalJugador}")
    return valorTotalJugador, valorCartasJugador


def asignarValorCrupier():
    global cartasCrupier
    global valorCartasCrupier
    global valorTotalCrupier
    valorCartasCrupier = []

    #Asignar valor a la mano del crupier, tomar los valores del diccionario y sumarlos, si es 'A' y el valor total de la mano es menor o igual a 10, se le asigna el valor de 11, si es mayor a 10, se le asigna el valor de 1
    for carta in cartasCrupier:
        valorCarta = valores[carta[0]]
        valorCartasCrupier.append(valorCarta) 
    valorTotalCrupier = sum(valorCartasCrupier)
    if 1 in valorCartasCrupier:
        if valorTotalCrupier <= 10:
            valorTotalCrupier = valorTotalCrupier + 10
            print(f"El valor de la mano del crupier es: {valorTotalCrupier}")
    print(f"El valor de la mano del crupier es: {valorTotalCrupier}\n")
    
    #Si el valor total de la mano del crupier es menor a 16, se le asigna una nueva carta
    while valorTotalCrupier < 16:
        print(f"El crupier pide una nueva carta.")
        time.sleep(1)
        cartaNueva = random.choice(obtenerBaraja())
        cartasCrupier.append(cartaNueva)
        valorCartaNueva = valores[cartaNueva[0]]
        valorCartasCrupier.append(valorCartaNueva)
        valorTotalCrupier = sum(valorCartasCrupier)
        print(f"La nueva carta del crupier es: {cartaNueva}")
        print(f"El valor de la mano del crupier es: {valorTotalCrupier}\n")
        time.sleep(1)
        if 1 in valorCartasCrupier:
            if valorTotalCrupier <= 10:
                valorTotalCrupier = valorTotalCrupier + 10
                print(f"El valor de la mano del crupier es: {valorTotalCrupier}")
            else:
                print(f"El valor de la mano del crupier es: {valorTotalCrupier}")

    return valorTotalCrupier, valorCartasCrupier    


def verificarGanador():
    global valorTotalJugador
    global valorTotalCrupier
    global apuesta
    global dineroJugador

    #Verificar si el jugador o el crupier ganan, si el jugador gana, se le suma la apuesta al saldo del jugador, si el crupier gana, se le resta la apuesta al saldo del jugador
    if valorTotalJugador > valorTotalCrupier and valorTotalJugador <= 21:
        dineroJugador = dineroJugador + apuesta
        print(f"Ganaste, tu nuevo saldo es de: ${dineroJugador}")
    elif valorTotalCrupier > valorTotalJugador and valorTotalCrupier <= 21:
        dineroJugador = dineroJugador - apuesta
        print(f"Perdiste, tu nuevo saldo es de: ${dineroJugador}")
    elif valorTotalJugador > 21 and valorTotalCrupier <= 21:
        dineroJugador = dineroJugador - apuesta
        print(f"Perdiste, tu nuevo saldo es de: ${dineroJugador}")
    elif valorTotalCrupier > 21 and valorTotalJugador <= 21:
        dineroJugador = dineroJugador + apuesta
        print(f"Ganaste, tu nuevo saldo es de: ${dineroJugador}")
    elif valorTotalJugador == 21 and valorTotalCrupier == 21:
        print(f"Empate, ambos alcanzaron 21, tu saldo actual es de: ${dineroJugador}")
    elif valorTotalJugador == valorTotalCrupier:
        print(f"Empate, tu saldo actual es de: ${dineroJugador}")
    return dineroJugador    



def dividirJugada():
    global valorTotalCrupier
    global cartasJugador
    global cartasJugador1
    global cartasJugador2
    global cartaJugador1
    global cartaJugador2
    global cartaJugador3
    global cartaJugador4
    
    global apuesta
    global dineroJugador

    baraja = obtenerBaraja()

    cartaJugador3 = baraja.pop()
    cartaJugador4 = baraja.pop()
    #Si el jugador tiene dos cartas iguales, se le asignan dos cartas más, una a cada mano
    cartasJugador1 = [cartaJugador1, cartaJugador3]
    cartasJugador2 = [cartaJugador2, cartaJugador4]

    #Si el jugador divide la jugada, se le asigna un nuevo valor a cada mano y se le resta la apuesta al saldo del jugador
    if cartaJugador1[0] == cartaJugador2[0]:
        while True:
            try:
                opcion = int(input("¿Deseas dividir tu jugada? Presiona 1 (sí), presiona 2 (no): "))
            except ValueError:
                print("Lo sentimos, debes ingresar un número entero.")
                continue
            if opcion == 1:
                if cartaJugador1[0] == cartaJugador2[0]:
                    time
                    print(f"\nTu primera mano es: {cartasJugador1}")
                    print(f"Tu segunda mano es: {cartasJugador2}")
                    dineroJugador = dineroJugador - apuesta
                    time
                    print(f"Tu nuevo saldo actual es: ${dineroJugador}")
                    time.sleep(1)
                    valorTotalJugador1 = asignarValorJugadorJugadaDividida(cartasJugador1)
                    valorTotalJugador2 = asignarValorJugadorJugadaDividida(cartasJugador2)
                    asignarValorCrupier()

                    #Se le asigna un nuevo valor a cada mano y se verifica si el jugador o el crupier ganan, si el jugador gana, se le suma la apuesta al saldo del jugador, si el crupier gana, se le resta la apuesta al saldo del jugador
                    if valorTotalJugador1 > valorTotalCrupier and valorTotalJugador1 <= 21:
                        dineroJugador = dineroJugador + apuesta
                        print(f"Resultado 1. Ganaste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalCrupier > valorTotalJugador1 and valorTotalCrupier <= 21:
                        dineroJugador = dineroJugador - apuesta
                        print(f"Resultado 1. Perdiste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalJugador1 > 21 and valorTotalCrupier <= 21:
                        dineroJugador = dineroJugador - apuesta
                        print(f"Resultado 1. Perdiste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalCrupier > 21 and valorTotalJugador1 <= 21:
                        dineroJugador = dineroJugador + apuesta
                        print(f"Resultado 1. Ganaste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalJugador1 == 21 and valorTotalCrupier == 21:
                        print(f"Resultado 1. Empate, ambos alcanzaron 21, tu saldo actual es de: ${dineroJugador}")
                    elif valorTotalJugador1 == valorTotalCrupier:
                        print(f"Resultado 1. Empate, tu saldo actual es de: ${dineroJugador}")
                    if valorTotalJugador2 > valorTotalCrupier and valorTotalJugador1 <= 21:
                        dineroJugador = dineroJugador + apuesta
                        print(f"Resultado 2. Ganaste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalCrupier > valorTotalJugador2 and valorTotalCrupier <= 21:
                        dineroJugador = dineroJugador - apuesta
                        print(f"Resultado 2. Perdiste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalJugador2 > 21 and valorTotalCrupier <= 21:
                        dineroJugador = dineroJugador - apuesta
                        print(f"Resultado 2. Perdiste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalCrupier > 21 and valorTotalJugador2 <= 21:
                        dineroJugador = dineroJugador + apuesta
                        print(f"Resultado 2. Ganaste, tu nuevo saldo es de: ${dineroJugador}")
                    elif valorTotalJugador2 == 21 and valorTotalCrupier == 21:
                        print(f"Resultado 2. Empate, ambos alcanzaron 21, tu saldo actual es de: ${dineroJugador}")
                    elif valorTotalJugador2 == valorTotalCrupier:
                        print(f"Resultado 2. Empate, tu saldo actual es de: ${dineroJugador}")
                    print(f"\nTu saldo final de esta partida es: ${dineroJugador}")
                    break       
                else:
                    print("Lo sentimos, no puedes dividir tu jugada.")
                    continue
            elif opcion == 2:
                print(f"Tu saldo actual es: ${dineroJugador}")
                break
            else:
                print("Lo sentimos, debes ingresar un número entero.")
                continue
        rondaJugada()


def asignarValorJugadorJugadaDividida(cartasJugador):
    valorCartasJugador = []

    #Asignar valor a la mano del jugador, tomar los valores del diccionario y sumarlos, si es 'A' preguntar si desea que valga 1 u 11, recibe como parametro la mano del jugador y retorna el valor de esta
    for carta in cartasJugador:
        valorCarta = valores[carta[0]]
        valorCartasJugador.append(valorCarta)
    valorTotalJugador = sum(valorCartasJugador)
    if 1 in valorCartasJugador:
        while True:    
            try:
                opcion = int(input("¿Deseas que el As valga 1 u 11?: "))
            except ValueError:
                print("Lo sentimos, debes ingresar un número entero.")
                continue
            if opcion == 1:
                valorTotalJugador = valorTotalJugador
                break
            elif opcion == 11:
                valorTotalJugador = valorTotalJugador + 10
                break
            else:
                print("Lo sentimos, debes ingresar un número entero.")
                continue
    print(f"El valor de tu mano es: {valorTotalJugador}")
    return valorTotalJugador



def rondaJugada():
    while True:
        #Preguntar si desea jugar una nueva ronda
        try:
            opcion = int(input("¿Deseas iniciar una jugada? Presiona 1 (sí), presiona 2 (no): "))
        except ValueError:
            print("Lo sentimos, debes ingresar un número entero.")
            continue
        #Si el jugador desea jugar una nueva ronda, se verifica si tiene el monto mínimo para jugar, se le pregunta el monto de su apuesta y se le reparten las cartas, se asignan valores y se verifica el ganador
        if opcion == 1:
                verificarDinero()
                obtenerApuesta()
                repartirCartas()
                asignarValorJugador()
                asignarValorCrupier()
                verificarGanador()
        else:
            write= 0
            listaDinero[review] = str(dineroJugador)
            print(f"Tu nuevo saldo actual es: ${dineroJugador}")
            with open("usuariosPrueba.txt", "w") as archivo:
                for i in listaUsuarios:
                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace("\n", ""))
                    archivo.write("\n")
                    write = write + 1
            print("Gracias por jugar.")
            #CAMBIAAAAARRRR DEBE VOLVER AL SUBMENU DE JUEGOS
            sys.exit()


def principalBlackJack():
    #Mostrar instrucciones del juego
    print('''Bienvenido al juego de Blackjack
          
    Instrucciones:
    El jugador juega contra el crupier (computadora)
    El jugador gana si suma 21 puntos o si el crupier se pasa de 21 puntos
    El jugador pierde si se pasa de 21 puntos o si el crupier suma 21 puntos
    El jugador empata si el jugador y crupier suman 21 puntos o si ambos tienen el mismo puntaje
    Si obtienes dos cartas iguales, puedes dividir la partida, para esto debes doblar la apuesta.
    Después de iniciada la jugada puedes decidir si doblar la apuesta o mantenerla
    Después puedes pedir cuantas cartas necesites, recuerda que si pasas de 21 pierdes!!!
    
    ''')

    rondaJugada()


#######################################################
#Verificar que el jugador tenga el mínimo de dinero para poder jugar

def obtenerFiguras():
    figuras = ["@", "@", "@", "@", "#", "#", "#", "+", "+", "7"]
    figurasObtenidas = []
    for i in range(3):
        figuraAleatoria = random.choice(figuras)
        figurasObtenidas.append(figuraAleatoria)
        print(figurasObtenidas)
        time.sleep(1.5)
    return figurasObtenidas


def ejecutarJugada():
    global acumulado, contador
    dineroJugador = listaDinero[review]
    dineroJugador = float(dineroJugador)
    while True:
        obtenerApuesta()
        input("Presiona enter para jalar la palanca e iniciar el juego...")
        time.sleep(1)

        contador += 1
        figurasObtenidas = []

        if contador == 5:
                for i in range(3):
                    figuraAleatoria = "@"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)

        elif contador == 10:
                for i in range(3):
                    figuraAleatoria = "#"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)

        elif contador == 15:
                for i in range(3):
                    figuraAleatoria = "+"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)

        elif contador == 20:
                for i in range(3):
                    figuraAleatoria = "7"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)
                    contador = 0
        else:
            figurasObtenidas = obtenerFiguras()


        if figurasObtenidas[0] == figurasObtenidas[1] == figurasObtenidas[2]:
            if figurasObtenidas[0] == "7":
                print(f"¡¡¡Pegaste el acumulado de: ${acumulado}")
                dineroJugador = dineroJugador - apuesta + acumulado
                acumulado = 0
            print("¡¡¡Felicidades!!! Ganaste la jugada.")
            dineroJugador = dineroJugador - apuesta + (apuesta * valorFiguras[figurasObtenidas[0]])
            print(f"Tu saldo actual es: ${dineroJugador}")

        else:
            print("Lo sentimos, no ganaste la jugada.")
            dineroJugador -= apuesta
            acumulado += apuesta
            print(f"Tu saldo actual es: ${dineroJugador}")
            if dineroJugador < apuestaMinima:
                print("Lo sentimos, no tienes saldo suficiente para jugar. Gracias por participar.")
                sys.exit()


def principal():
    print('''\nBienvenido a la maquina tragamonedas!!!   
            
    Reglas:
        1. Para poder jugar debes apostar un monto mínimo y máximo.
        2. Presionarás enter para jalar la palanca e iniciar la jugada.
        3. Se mostrarán las figuras obtenidas.
        4. Si aparecen 3 "@", recuperas lo invertido.
        5. Si aparecen 3 "#", ganas el doble de lo invertido.
        6. Si aparecen 3 "+", ganas el triple de lo invertido.
        7. Si aparecen 3 "7", ganas el acumulado.
          
        Éxitos!!!
        ''')      

    while True:
        verificarDinero()
        ejecutarJugada()

########################################################

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
                decision = int(input("Seleccione 1 para jugar BlackJack \nSeleccione 2 para jugar Tragamonedas \nSeleccione 3 para salir al menu"))
                if decision == 1:
                    principalBlackJack()
                elif decision == 2:
                    principal()
                elif decision == 3:
                    subMenu(usuario)
                #principalBlackJack(dineroDisponible)
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
dineroJugador = listaDinero[review]
dineroJugador = float(dineroJugador)
subMenu(usuario)
>>>>>>> Stashed changes
