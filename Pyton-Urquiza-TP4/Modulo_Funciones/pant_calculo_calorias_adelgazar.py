from ConCalAdelgazar import consumo_calorias_recomendado_para_adelgazar
from TmbApp import calcular_calorias_en_reposo
from calculadora_indices import peso, altura, genero, edad

# Calculo de las calorias para adelgazar
TMB = calcular_calorias_en_reposo(peso, altura, edad, genero)
Calorias_Adelgazar = consumo_calorias_recomendado_para_adelgazar(TMB)
print(Calorias_Adelgazar)
