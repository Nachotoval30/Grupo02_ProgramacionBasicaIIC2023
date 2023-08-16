import random
import time
import sys

#Se deben cargar de la configuracion avanzada
apuestaMinima = 100
dineroJugador = 2000

acumulado = 0
contador = 0
apuesta = 0

#Valor por el que se multiplica la apuesta del jugador en caso de ganar la jugada (3 figuras iguales)
valorFiguras = {
    "@": 1,
    "#": 2,
    "+": 3,
    "7": acumulado
}


#Verificar que el jugador tenga el mínimo de dinero para poder jugar
def verificarDinero():
    global dineroJugador
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
    while True:
        try:
            opcion = int(input("Para jugar presiona 1, para salir presiona 2:  "))
        except ValueError:
            print("Lo sentimos, debes ingresar un número entero.")
            continue
        if opcion == 2:
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
    global dineroJugador, acumulado, contador

    while True:
        obtenerApuesta()
        input("Presiona enter para jalar la palanca e iniciar el juego...")
        time.sleep(1)

        contador += 1
        figurasObtenidas = []

        if contador == 1:
                for i in range(3):
                    figuraAleatoria = "@"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)

        elif contador == 2:
                for i in range(3):
                    figuraAleatoria = "#"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)

        elif contador == 4:
                for i in range(3):
                    figuraAleatoria = "+"
                    figurasObtenidas.append(figuraAleatoria)
                    print(figurasObtenidas)
                    time.sleep(1.5)

        elif contador == 5:
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
principal()
