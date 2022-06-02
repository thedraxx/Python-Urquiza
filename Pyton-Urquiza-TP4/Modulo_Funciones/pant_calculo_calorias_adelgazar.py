from calculadora_indices import consumo_calorias_recomendado_para_adelgazar, calcular_calorias_en_reposo, peso, altura, edad, genero

# Calculo de las calorias para adelgazar
TMB = calcular_calorias_en_reposo(peso, altura, edad, genero)
Calorias_Adelgazar = consumo_calorias_recomendado_para_adelgazar(TMB)
print(Calorias_Adelgazar)
