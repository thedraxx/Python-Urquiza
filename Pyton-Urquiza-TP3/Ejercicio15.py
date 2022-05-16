def UltPalabra(cadena):
    longitud = len(cadena)
    if longitud == 0:
        return 0
    cantidad = 0
    for i in range(longitud):
        if cadena[i] != ' ':
            cantidad += 1
        else:
            if cadena[i] == ' ' and i < (longitud-1) and cadena[i+1] != ' ':
                cantidad = 0
    return cantidad


def DNIvalido(dni):
    if len(str(dni)) <= 6 or len(str(dni)) >= 9:
        return True


def primerosTresDigitos(numero):
    while numero >= 1000:
        numero = numero // 10
    return numero


def obtenerId(nombre, dni):
    nombre = nombre.strip()
    id = nombre[:nombre.find(" ")]
    id = id+str(UltPalabra(nombre))
    id = id+str(primerosTresDigitos(dni))
    return id

nombre = input("Nombre del socio: ")
while nombre != "":
    dni = int(input("DNI del socio: "))
    while DNIvalido(dni):
        print("DNI inválido. Intente de nuevo")
        dni = int(input("DNI del socio: "))
    print(obtenerId(nombre, dni))
    nombre = input("Nombre del socio: ")
