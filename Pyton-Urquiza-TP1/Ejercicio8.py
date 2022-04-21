n = int(input('ingrese la cantidad de piezas'))
contp = int(0)
for x in range(n):
    m = float(input('ingrese las medidas:'))
    if m >= 1.20 and m <= 1.30:
        contp +=1
print('cantidad de piezas que son aptas:',contp)