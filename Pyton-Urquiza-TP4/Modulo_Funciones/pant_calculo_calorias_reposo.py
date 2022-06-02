from calculadora_indices import peso, altura, genero, edad, calcular_calorias_en_reposo

# Tasa metabólica basal
TMB = calcular_calorias_en_reposo(peso, altura, edad, genero)
print('Valor Tasa metabólica basal: ', TMB)
