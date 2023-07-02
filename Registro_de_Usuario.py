#Creacion de nombre de ususraio

def obtener_id():
    intentos = 0
    while intentos < 3:
        ID = input("Ingrese un ID alfanumerico de al menos 5 cararcteres: ")
        if len(ID) >= 5 and ID.isalnum():
           return ID
        else:
            print("El ID ingresado debe tener 5 caracteres, Intentelo de Nuevo")
            intentos += 1
    print("Has excedido el número máximo de intentos. Regresando al menú principal.")
   

ids_usuarios = set()

while True:
    id_ususario = obtener_id()
    if id_ususario in ids_usuarios:
        print("El ID ya existe, Ingrese otro.")
    else:
        ids_usuarios.add(id_ususario)
print("Su ID es: ")
for id in ids_usuarios:
    print(id)
    
