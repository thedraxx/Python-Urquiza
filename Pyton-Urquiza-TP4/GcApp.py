valor_genero = 0


def TableGC(Gc, genero, edad):
    if genero == 'M':
        if edad >= 20 and edad <= 29:
            return ('rango GC recomendado: 11% _ 20%')
        if edad >= 30 and edad <= 39:
            return ('rango GC recomendado: 12% _ 21%')
        if edad >= 40 and edad <= 49:
            return ('rango GC recomendado: 14% _ 23%')
        if edad >= 50 and edad <= 59:
            return ('rango GC recomendado: 14% _ 23%')
    elif genero == 'F':
        if edad >= 20 and edad <= 29:
            return ('rango GC recomendado: 16% _ 28%')
        if edad >= 30 and edad <= 39:
            return ('rango GC recomendado: 17% _ 29%')
        if edad >= 40 and edad <= 49:
            return ('rango GC recomendado: 18% _ 30%')
        if edad >= 50 and edad <= 59:
            return ('rango GC recomendado: 19% _ 31%')

def Gc(IMC, edad, genero):
    lista = [];
    if(genero == 'F'):
        valor_genero = 10.8
    else:
        valor_genero = 0
    Gc = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero
    tabla = TableGC(Gc, genero, edad)
    lista = [Gc,tabla]
    return lista
   
