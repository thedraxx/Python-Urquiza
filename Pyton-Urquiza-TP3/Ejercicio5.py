

p = int(input("Coloque el lado de un cuadrado"))
perimetro = 0
superficie = 0
opcion = input(" p o s ")

def calcularPerimetro(p):
    perimetro = p * 4
    return perimetro


def calcularSuperficie(p):
    superficie = p * 2
    return superficie

if(opcion == "p"):
    print(calcularPerimetro(p))

elif (opcion == "s"):
    print(calcularSuperficie(p))


