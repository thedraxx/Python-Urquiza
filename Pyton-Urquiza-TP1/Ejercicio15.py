u = input('ingrese un nombre')
p = input('ingrese una contra')
c = int(0)

if len(u) >= 6 and len(p) <=12:
    if len(p) >= 8 :
        for i in p:
            if i != " ":
                c += 1
if c > 0:
    print('usuario registrado')
else:
    print('usuario no registrado')
    