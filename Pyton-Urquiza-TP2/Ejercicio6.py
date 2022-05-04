n = int(input('ingrese un numero: '))
lp = list()
hp = list()
for x in range(n):
    p = (input('ingrese un pais: '))
    lp.append(p)
    h = int(input('ingrese la cantida de habitantes: '))
    hp.append(h)

hp.sort(reverse=True)
print(hp, 'sex')
