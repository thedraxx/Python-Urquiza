n = input('ingrese su nombre')
n = n.upper()
vocal = ('A', 'E', 'I', 'O', 'U')
letra = n[0]
if letra in (vocal):
    print('arranca con vocal')
else:
    print('no arranca con vocal')