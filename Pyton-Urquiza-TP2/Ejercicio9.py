p = input('ingrese un nombre; ')

p = ''.join(p.split())
print(p)

msj = p[0: 5]
msj += "@"

print(msj, "la palabra entera es: ", p)
