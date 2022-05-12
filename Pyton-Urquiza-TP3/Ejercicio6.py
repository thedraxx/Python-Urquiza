

p = int(input("Coloque el lado de un cuadrado"))
perimetro = 0
superficie = 0
opcion = input(" p o s ")

def calcularPerimetro(p):
    perimetro = p * 4
    return mostrarResultado(perimetro)

def calcularSuperficie(p):
    superficie = p * 2
    return mostrarResultado(superficie)
    
def mostrarResultado(resultado):
     print(resultado)

if(opcion == "p"):
    calcularPerimetro(p)

elif (opcion == "s"):
    calcularSuperficie(p)

