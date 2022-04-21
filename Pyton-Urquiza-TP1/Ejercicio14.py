n = int(input('ingrese la cantidad de triangulos que va a ingresar:'))
conteq = int(0)
conti = int(0)
conte = int(0)
for x in range(n):
    l = int(input('ingrese un lado:'))
    l2 = int(input('ingrese un lado:'))
    l3 = int(input('ingrese un lado:'))
    if l == l2 and l == l3 and l2 == l3:
        print('es equilatero')
        conteq +=1
    elif l == l2 or l == l3 or l2 == l3:
        print('es isoceles')
        conti += 1
    else:
        print('es escaleno')
        conte +=1
print('cantidad de triangulos equilateros:',conteq)
print('cantidad de triangulos isoceles:',conti)
print('cantidad de triangulos escaleno:',conte)