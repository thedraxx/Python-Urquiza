n = int(input('Ingrese la cantidad de personas'))
a = int(0)
for x in range(n):
    p = int(input('Ingrese la altura de la persona'))
    a = a + p

promedio = int(a/n)
print('el promedio es',promedio)
