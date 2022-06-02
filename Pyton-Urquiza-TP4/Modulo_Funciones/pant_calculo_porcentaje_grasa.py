from calculadora_indices import peso, altura, genero, edad, calcular_IMC, calcular_porcentaje_grasa

# Porcentaje Grasa Corporal:
IMC = calcular_IMC(peso, altura)
GC = calcular_porcentaje_grasa(IMC, edad, genero)
print('Valor Porcentaje Grasa Corporal: ', GC)
