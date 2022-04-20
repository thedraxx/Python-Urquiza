n = int(input('ingrese la cantidad de empleados'))
valor = int(0)
valor2 = int(0)
c = int(0)
c2 = int(0)

for x in range(n):
    s = int(input('ingrese el sueldo de los empleados'))
    if s >= 100 and s <= 300:
        c += 1
        valor = valor + c
    elif s > 300:
        valor2 = valor2 + s
        c2 +=1

print('Las personas que ganan entre 100 y 300 son',c)
print('Las personas que ganan mas de 300 son',c2)
print('Las empresa gasta en sueldos', valor + valor2)