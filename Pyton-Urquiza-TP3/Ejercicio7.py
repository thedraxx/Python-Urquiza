from funcionesEjercicio7 import calcularPerimetro, calcularSuperficie, mostrarResultado 

p = int(input("Coloque el lado de un cuadrado"))
perimetro = 0
superficie = 0
opcion = input(" p o s ")

if(opcion == "p"):
    calcularPerimetro(p)

elif (opcion == "s"):
    calcularSuperficie(p)
