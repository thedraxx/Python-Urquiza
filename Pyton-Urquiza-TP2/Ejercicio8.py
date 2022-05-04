n = int(input('ingrese un numero de alumnos: '))
lp = list()
hp = list()
max = int(0)
for x in range(n):
    p = (input('ingrese un nombre: '))
    lp.append(p)
    pr = int(input('ingrese nota: '))
    if(pr >= 8):
        print("muy bueno")
        max = max + 1
    if(pr >= 4 and pr <= 7):
        print("bueno")
    if(pr < 4):
        print("insuficiente")


print("cantidad de muy buenos", max)
