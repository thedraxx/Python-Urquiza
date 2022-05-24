from ImcApp import IMC 
from GcApp import Gc

print('Bienvenido.')
peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))
edad = int(input('Ingrese su edad: '))
genero = input('Ingrese su genero: (F o M) ')

IMC = IMC(peso,altura)
print (IMC[1])

GC = Gc(IMC[0],edad,genero)
print(GC)

