
# def ImcValue(Imc):
#     if Imc < 16:
#         return('Delgadez severa')
#     if Imc >= 16 and Imc < 16.99:
#         return('Delgadez moderada')
#     if Imc >= 17 and Imc < 18.49:
#         return('Delgadez aceptable')
#     if Imc >= 18.5 and Imc < 24.99:
#         return('Peso normal')
#     if Imc >= 25 and Imc < 29.99:
#         return('Sobrepeso')
#     if Imc >= 30 and Imc < 34.99:
#         return('Obesidad tipo I')
#     if Imc >= 35 and Imc < 39.99:
#         return('Obesidad tipo II')
#     if Imc >= 40 and Imc < 49.99:
#         return('Obesidad tipo III o Morbida')
#     if Imc >= 50:
#         return('Obesidad tipo IV o Extrema')

def calcular_IMC(peso, altura):
    Imc = peso / (altura * altura)
    return round(Imc)
