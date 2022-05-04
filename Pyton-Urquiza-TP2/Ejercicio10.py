n = int(input('ingrese un numero de empleados: '))
lp = 0
max = int(0)
emp = str("")

for x in range(n):
    p = (input('ingrese nombre: '))
    for j in range(3):
        sueldo = int(input('ingrese seldo:'))
        lp += sueldo
    print("Sueldo acumulado: ", lp)
    lp = 0
    if(max < sueldo):
        max = sueldo
        emp = p

print("El mejor sueldo lo tiene", emp)
