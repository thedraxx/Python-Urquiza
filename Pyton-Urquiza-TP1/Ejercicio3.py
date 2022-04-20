preg = int(input('Ingrese la cantidad de preguntas:'))
pregb = int(input('Ingrese la cantidad de preguntas correctas:'))

porc = 100 * (pregb / preg)

if porc >= 90:
    print('Nivel Maximo')
elif porc >= 75 and porc < 90:
    print('Nivel medio')
elif porc >= 50 and porc < 75:
    print('Nivel regular')
elif porc < 50:
    print('Fuera de nivel')