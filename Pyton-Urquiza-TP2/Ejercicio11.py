n = int(input('ingrese cantidad de paises '))
lp = 0
max = int(0)
emp = str("")

for x in range(n):
    p = (input('ingrese nombre de pais: '))
    for j in range(3):
        temperatura = int(input('ingrese tres temperaturas medias mensuales:'))
        lp += temperatura
    print("Pais: ", p, "Temperatura: ", lp)
    lp = 0
    if(max < temperatura):
        max = temperatura
        emp = p

print("La temperatura del pais con la mayor temperatura media trimestral es: ", emp)
