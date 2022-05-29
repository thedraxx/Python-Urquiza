from Tmb_FisicaApp import calcular_calorias_en_actividad
from calculadora_indices import actividadFisica, peso, altura, genero, edad
from TmbApp import calcular_calorias_en_reposo

#  metabólica basal según actividad física
TMB = calcular_calorias_en_reposo(peso, altura, edad, genero)
TMB_FISICA = calcular_calorias_en_actividad(TMB, actividadFisica)
print('Valor metabólica basal según actividad física: ', TMB_FISICA)
