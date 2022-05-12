precio = int(input("Ingrese precio por metro de alambre"))
medidaAlto = int(input("Ingrese el alto en metros"))
medidaAncho = int(input("Ingrese el ancho en metros"))

def caulculos(precio, medidaAlto, medidaAncho):
    metroTotal = medidaAlto + medidaAncho
    precioTotal = precio * metroTotal
    return precioTotal

print (caulculos(precio, medidaAlto, medidaAncho))
