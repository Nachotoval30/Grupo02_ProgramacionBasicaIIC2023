id = ""
pin = ""
usuario = ""
review = 0
intentos = 0
dineroDisponible = 0
listaUsuarios = []
listaPassword = []
listaDinero = []

def separarlista():
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

def limpiar():
    listaUsuarios = []
    listaPassword = []
    listaDinero = []
    return listaUsuarios, listaPassword, listaDinero

def revisarSaldo():
    #Para realizarlo vamos a llamar a la funcion que separa en listas las bases de datos
    #y devuelve el index del que se quiere buscar para obtener el dinero en especifico
    review = 2
    #listaUsuarios, listaPassword, listaDinero= separarlista()
    dineroDisponible = listaDinero[review]
    print("Dinero disponible", dineroDisponible)
    #listaUsuarios, listaPassword, listaDinero= limpiar()
    return float(dineroDisponible)

def depositar():
    separarlista()
    listaDivisa = []
    review = 3
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
                            print("depositoreal", deposito)
                            listaDinero[review] = str(deposito)
                            with open("usuariosPrueba.txt", "w") as archivo:
                                for i in listaUsuarios:
                                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",",""))
                                    archivo.write("\n")
                                    write = write + 1

                except ValueError:
                    count = count +1     
                
            
            
            elif decision == 2:
                try:
                    deposito = float(input("Digite la cantidad de Dolares para depositar"))
                        #Al momento de la revision dos se encuentra en proceso la funcion de depositar dinero
                    print(f"El deposito en dolares a realizar es de {deposito}")
                    deposito = deposito + float(listaDinero[review])
                    deposito = round(deposito, 3)
                    print("depositoreal", deposito)
                    listaDinero[review] = str(deposito)
                    with open("usuariosPrueba.txt", "w") as archivo:
                        for i in listaUsuarios:
                            archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",",""))
                            archivo.write("\n")
                            write = write + 1
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
                            print("depositoreal", deposito)
                            listaDinero[review] = str(deposito)
                            with open("usuariosPrueba.txt", "w") as archivo:
                                for i in listaUsuarios:
                                    archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",",""))
                                    archivo.write("\n")
                                    write = write + 1


                except ValueError:
                            #la funcion revisar saldo se encuentra corriendo
                    count = count +1
                    print("test3")
            else:
                print("Elvalor ingresado no esta dentro de las opciones, intente de nuevo")
        except ValueError:
            count = count +1
            print("El valor ingresado no se encuentra dentro de las opciones, intentelo de nuevo")
    else:
        print("Excedio el maximo de intentos para realizar el deposito, volviendo al menu principal")        

def cambio():
    review = 2
    dineroRetirar = 1000
    count = 0
    #listaUsuarios, listaPassword, listaDinero= separarlista()
    listaDinero[review] = int(listaDinero[review]) - dineroRetirar
    #print(listaDinero)
    with open("usuariosPrueba.txt", "w") as archivo:
        for i in listaUsuarios:
            archivo.write(str([listaUsuarios[count], listaPassword[count], listaDinero[count]]).replace("'", "").replace("[", "").replace("]", "").replace(",",""))
            archivo.write("\n")
            count = count + 1
    print("El dinero retirado es de:", dineroRetirar)
    #listaUsuarios, listaPassword, listaDinero= limpiar()
    archivo.close()

def eliminarUsuario():
    write = 0
    review = 2
    dineroDisponible = revisarSaldo()
    print(dineroDisponible)
    if dineroDisponible == 0:
        print("aqui")
        listaUsuarios.pop(review)
        listaPassword.pop(review)
        listaDinero.pop(review)
        print(listaUsuarios)
        print(listaPassword)
        print(listaDinero)
        with open("usuariosPrueba.txt", "w") as archivo:
            for i in listaUsuarios:
                archivo.write(str([listaUsuarios[write], listaPassword[write], listaDinero[write]]).replace("'", "").replace("[", "").replace("]", "").replace(",",""))
                archivo.write("\n")
                write = write + 1
    else:
        print("Debe retirar todo el dinero en la cuenta antes de eliminar la misma")
        #submenu

listaUsuarios, listaPassword, listaDinero= separarlista()
cambio()
eliminarUsuario()
#depositar()
#separarlista()
