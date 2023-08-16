import random
import time
import sys

#Global Variables
dineroJugador = 1000
apuestaMinima = 50
apuesta = 0

#Figuras y valores de las cartas
figuras = ['♠', '♥', '♦', '♣']
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

def verificarDinero():
    global dineroJugador
    #Verificar si el jugador tiene el monto mínimo para jugar
    if dineroJugador < apuestaMinima:
        print(f"Lo sentimos, no tienes el monto mínimo para jugar. La apuesta minima es de: ${apuestaMinima}")
        #CAMBIAAAAARRRR DEBE VOLVER AL SUBMENU DE JUEGOS
        sys.exit()
    else:
        print(f"Tu saldo actual es: ${dineroJugador}")
        return dineroJugador
    

def obtenerApuesta():
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
            print("Gracias por jugar.")
            #CAMBIAAAAARRRR DEBE VOLVER AL SUBMENU DE JUEGOS
            sys.exit()


def principal():
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
principal()
