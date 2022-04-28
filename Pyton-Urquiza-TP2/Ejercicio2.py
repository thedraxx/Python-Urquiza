n = int(input('ingrese un numero: ')) 
lista = []
cont = 0

for x in range (n):
    sueldo = int(input("Ingrese su sueldo: "))
    lista.append(sueldo)
    if sueldo >= 2500 :
        cont +1
   

ordenar = sorted(lista)
print("Sueldo Ordenado: ", ordenar)
print("La cantidad de sueldos mayores o iguales a 2500 es: ", cont)