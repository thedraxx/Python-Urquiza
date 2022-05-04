n = int(input('ingrese un numero: '))
lp = list()
hp = list()
max = int(0)
for x in range(n):
    p = (input('ingrese un productos: '))
    lp.append(p)
    pr = int(input('ingrese precio: '))
    hp.append(pr)
    if (hp[0] < pr):
        max = +1

print("la cantidad de productos mayores al primero son", max)
