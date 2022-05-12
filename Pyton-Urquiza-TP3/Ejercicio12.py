capital = int(input("ingrese capital"))
dias = int(input("ingrese dias"))
tasa = int(input("ingrese tasa"))

def interesSimple(tasa,dias,capital):
    resultado = (tasa * dias * capital) / 100
    return resultado

print(interesSimple(tasa,dias,capital))
