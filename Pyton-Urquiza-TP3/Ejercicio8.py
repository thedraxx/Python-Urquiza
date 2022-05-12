
def maximo(x,y):
    if x>y:
        return x
    else:
        return y

def minimo(x,y):
    if x<y:
        return x
    else:
        return y

#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))
