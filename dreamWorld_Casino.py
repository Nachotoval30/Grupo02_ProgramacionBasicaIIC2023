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
picas = '♠'
corazones = '♥'
diamantes = '♦'
treboles = '♣'

valorFiguras = {
    "@": 1,
    "#": 2,
    "+": 3,
    "7": acumulado
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
def principalBlackJack(dineroJugador):
    dineroJugador = listaDinero[review]
    print("DINEEEROO", dineroJugador)
    #Se imprimen las reglas del juego
    print('''\nBienvenido al Blackjack!!!   
            
    Reglas:
        1. Para poder jugar debes apostar un monto mínimo, el cual se te indicará más adelante (no hay límite máximo).
        2. El crupier entregará 4 cartas, 2 para la casa y 2 para el usuario.
        3. Después de haber iniciar la partida, podrá doblar la apuesta si así lo desea.
        4. Si obtienes dos cartas iguales, podrás decidir si dividir la partida.
        5. Luego podrás pedir más cartas mientras tu puntuación sea menor a 21.
        6. El juego termina si deseas parar o su tus cartas suman más de 21.
        7. Posterior, el crupier muestra la carta oculta.
        8. Gana el que más se acerque a 21 sin pasar dicho número.
        9. Si gana se le duplica el monto apostado, si es empate se le devuelve dicho monto y si pierde no se le devuelve nada.
          
        Éxitos!!!
        ''')
    
    #Ciclo principal dentro de la función
    while True:
        #Revisar que el jugador tenga dinero
        if int(dineroJugador) <= 0:
            print("DINEEEEROOOOO2", dineroJugador)
            print('No tienes dinero en tu cuenta, necesitas un monto mínimo para poder realizar una apuesta!!')
        #TIENE QUE SALIR AL MENU PRINCIPAL, CAMBIARLOOOOOOOOOOOOOOOO
            sys.exit()

        #Permitir al usuario que ingrese la apuesta
        print(f'El dinero en tu cuenta es: {dineroJugador}')
        apuesta = apuestaJugador(apuestaMinima)

        #Se obtiene baraja desde una función y se le asignan las cartas al crupier y jugador
        baraja = obtenerBaraja()
        time.sleep(1)
        cartaJugador1 = [baraja.pop()] 
        cartaJugador2 = [baraja.pop()]
        cartaDealer1 = [baraja.pop()]
        cartaDealer2 = [baraja.pop()]

        #Se realiza la suma de las cartas
        cartasJugador = (cartaJugador1 + cartaJugador2)
        cartasDealer = (cartaDealer1 + cartaDealer2)

        print('\nApuesta: ', apuesta)

        #ACCIONES DEL JUGAODR
        while True:
            #Se imprimen las cartas de una por una, dejando oculta la primera del crupier
            print('')
            time.sleep(1)
            print('Jugador 1: ', cartaJugador1)
            time.sleep(1)   
            print('Crupier 1: carta oculta')
            time.sleep(1)
            print('Jugador 2: ', cartaJugador2)
            time.sleep(1)
            print('Crupier 2: ', cartaDealer2)
            time.sleep(1)
            mostrarJugada(cartasJugador, cartasDealer, False)
            print('')

            if valorCarta(cartasJugador) > 21:
                break
                
            #Obtener el movimiento que realiza el jugador y se le descuenta al dinero lo apostado
            movimiento = obtenerMovimiento(cartasJugador, dineroJugador - apuesta)

            #Manejar las acciones del jugador
            if movimiento == 'D' and dineroJugador < apuestaMinima:
                print('No tienes dinero suficiente en tu cuenta para realizar la apuesta mínima')
                break
            elif movimiento == 'D':
                #Jugador esta doblando la apuesta, asi que la puede incrementar
                otraApuesta = apuestaJugador(apuestaMinima)
                apuesta += otraApuesta
                print(f'Apuesta incrementó a: {apuesta}')
                print('Apuesta: ', apuesta)

            if movimiento in ('H', 'D'):
                #El jugador selecciona otro hit e incrementa apuesta
                nuevaCarta = baraja.pop()
                numero, simbolo = nuevaCarta
                #Se imprime el valor obtenido en la nueva carta y se adjunta a las cartas del jugador
                print(f'\nCarta adicional: Obtuviste un {numero} de {simbolo}')
                cartasJugador.append(nuevaCarta)
                if valorCarta(cartasJugador) > 21:
                    continue
            if movimiento in ('S', 'D'):
                #El jugador se detiene e incrementa apuesta
                break

        
        #AACCIONES DEL CRUPIER
        if valorCarta(cartasJugador) <= 21:
            while valorCarta(cartasDealer) < 16:
                #Si las cartas del crupier suman menos de 16, se realiza un hit
                nuevaCartaDealer = baraja.pop()
                numero, simbolo = nuevaCartaDealer
                #La nueva carta se adjunta a las cartas del crupier
                cartasDealer.append(nuevaCartaDealer)
                time.sleep(1)
                print(f'El crupier realiza un hit, obtuvo un {numero} de {simbolo}')

                #print(cartasDealer)
                
                if valorCarta(cartasDealer) > 21:
                    break 
                time.sleep(1)
                input('Presiona Enter para continuar')
                print('\n\n')

        #Manejar las cartas al final
        mostrarJugada(cartasJugador, cartasDealer, True) 

        valorJugador = valorCarta(cartasJugador)
        valorDealer = valorCarta(cartasDealer)

        #Decisión del ganador 
        if valorDealer > 21:
            time.sleep(1)
            print(f'El crupier pasó de 21.... GANASTE ${apuesta}!!!!!')
            dineroJugador += apuesta
        elif valorJugador == valorDealer:
            time.sleep(1)
            print('Es un empate, se te devuelve la apuesta')
        elif (valorJugador < valorDealer) or (valorJugador > 21):
            time.sleep(1)
            print('PERDISTE!!')
            dineroJugador -= apuesta
        elif valorJugador > valorDealer:
            time.sleep(1)
            print(f'GANASTE ${apuesta}')
            dineroJugador += apuesta
        time.sleep(0.5)
        input('Presiona Enter para continuar')
        print('\n\n')

#Función para preguntar al usuario la apuesta, mencionando el monto mínimo
def apuestaJugador(apuestaMinima):
    #Preguntar al usuario cuanto quiere apostar este round
    while True:
        print(f'La apuesta mínima es de {apuestaMinima}. ¿Cuánto deseas apostar?')
        apuesta = input('Digita el monto o SALIR: ').upper().strip()

        if apuesta == 'SALIR': 
            print('Gracias por jugar!!!')
            sys.exit()
        #Si el usuario no ingresa un numero sigue el ciclo para volverle a preguntar 
        if not apuesta.isdecimal():
            continue 

        #El monto de la apuesta se convierte a entero, porque es válido que digite un string
        apuesta = int(apuesta)
        if apuesta >= apuestaMinima:
            return apuesta

        
#Función para obtener las cartas
def obtenerBaraja():
    baraja = []
    letraJ = 'J'
    letraQ = 'Q'
    letraK = 'K'
    letraA = 'A'
    #Este ciclo recorre los 4 simbolos y dentro de este los números correspondiente
    for simbolo in (picas, corazones, diamantes, treboles):
        for numero in range (2,11):
            baraja.append((str(numero), simbolo))
        for letra in (letraJ, letraQ, letraK, letraA):
            baraja.append((letra, simbolo))
    #Se acomodan al azar y se retorna la baraja completa de 52 cartas
    random.shuffle(baraja)
    return baraja        

#Función para mostrar las cartas
def mostrarJugada(cartasJugador, cartasDealer, mostrarCartaDealer):
    #Mostrar cartas jugador y crupier, ocultar la primer carta del crupier
    print('')
    if mostrarCartaDealer:
        time.sleep(1)
        print('Crupier tiene: ', cartasDealer)
        time.sleep(1)
        print('Suma cartas crupier: ', valorCarta(cartasDealer))
    else: 
        time.sleep(1)
        #Ocultar primera carta del crupier
        print('Crupier tiene: [(?, ?), {}]'.format(cartasDealer[1]) )
        time.sleep(1)
        print('Suma cartas crupier: ')

    #Mostrar cartas del jugador
    time.sleep(1)
    print('Jugador tiene: ', cartasJugador)
    time.sleep(1)
    print('Suma cartas jugador: ', valorCarta(cartasJugador))
        
#Función para asignar el valor a las cartas
def valorCarta(cartas):
    #Devolver el valor de las cartas con letra, que valen 10 y los As que pueden valer 1 o 11, depende de la situacion
    valor = 0
    cantidadAs = 0

    #Agregar el valor a las cartas que no son As
    for carta in (cartas):
        numero = carta[0]
        if numero == 'A':
            cantidadAs += 1
        elif numero in ('J', 'Q', 'K'): #Estas cartas valen 10
            valor += 10
        else: 
            valor += int(numero)
    #Agregar valor a los As de 11 si no sobrepasa 21
    valor += cantidadAs
    for i in range (cantidadAs):
        if valor + 10 <= 21:
            valor += 10
    return valor   

#Función para obtener del jugador la jugada que desea realizar
def obtenerMovimiento(cartasJugador, dineroJugador):
     while True:
        time.sleep(1)
        print('Debe seleccionar la letra del movimiento que desea realizar, H: obtener otra carta, S: detenerte, D: doblar apuesta')
        time.sleep(1)
        movimientos = ['(H)it', '(S)tand']

        #El jugador va a tener dos cartas
        if len(cartasJugador) == 2 and dineroJugador > 0:
            movimientos.append('(D)oblar apuesta') 
             
        #Preguntar que movimiento va a realizar
        promptMovimiento = ', '.join(movimientos) + ': '
        movimiento = input(promptMovimiento).upper()
        if movimiento in ('H', 'S'):
            return movimiento 
        if movimiento == 'D' and '(D)oblar apuesta' in movimientos:
            return movimiento

#######################################################
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
                principal()
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
subMenu(usuario)