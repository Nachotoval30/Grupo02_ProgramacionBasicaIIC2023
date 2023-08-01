import random
import sys
import time

#Simbolos de las cartas
picas = '♠'
corazones = '♥'
diamantes = '♦'
treboles = '♣'

#Estas variables se deben cargar desde la configuración avanzada
dineroJugador = 300
apuestaMinima = 200

#Función principal del juego
def principalBlackJack(dineroJugador):
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
        if dineroJugador <= 0:
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

principalBlackJack(dineroJugador)