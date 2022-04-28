
lista = ['rosario', 'buenos aires', 'carlos paz', 'santa fe']

c = input('ingrese el nombre de una ciudad: ')

v = (c in lista)

if v == True:
    print('la ciudad esta en la posición: ', lista.index(c))
else:
    print('ciudad no encontrada')    

 