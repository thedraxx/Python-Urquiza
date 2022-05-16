
from cgitb import reset


Articulo = input(' Ingrese  Articulo ')
Precio_Unitario = int(input(' Ingrese Precio Unitario '))
Cantidad = int(input(' Ingrese  cantidad '))


def CalcularDescuento(c,Articulo):
    resultado = c * 0.08
    return print("El producto", Articulo, "Cuesta con el descuento del 8% aplicado: ", (c - resultado))

def CalcularDescuentob(c,Articulo):
    resultado = c * 0.15
    return print("El producto", Articulo, "Cuesta con el descuento del 15% aplicado: ", (c - resultado))

def calcularPrecioTotal(Articulo, Precio_Unitario, Cantidad):
    c = 0
    for x in range(Cantidad):
        c = c + Precio_Unitario
    if(c < 15000):
        return ("El producto", Articulo, "vale", c)
    elif(c >= 15000):
        return CalcularDescuento(c, Articulo)
    elif(c >= 30000):
        return CalcularDescuentob(c, Articulo)
        

print(calcularPrecioTotal(Articulo, Precio_Unitario, Cantidad))
