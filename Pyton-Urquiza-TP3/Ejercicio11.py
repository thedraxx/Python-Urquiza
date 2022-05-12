palabra = input(" Ingrese oracion ")


def longitud(palabra):
    frase = palabra.split()
    return len(frase.pop())


print(longitud(palabra))