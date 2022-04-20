may = int(0)
mini = int(0)
n = int(input('Ingrese notas: '))
while n > 0:
    n = int(input('Ingrese notas: '))
    if n >= 7:
        may += 1
    elif n < 7:
        mini += 1
print('Cantidad de notas mayores a 7: ', may, 'y las menores', mini)
    