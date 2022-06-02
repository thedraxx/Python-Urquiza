from calculadora_indices import peso, altura, edad, genero, actividadFisica, calcular_calorias_en_actividad, calcular_calorias_en_reposo

#  metabólica basal según actividad física
TMB = calcular_calorias_en_reposo(peso, altura, edad, genero)
TMB_FISICA = calcular_calorias_en_actividad(TMB, actividadFisica)
print('Valor metabólica basal según actividad física: ', TMB_FISICA)
