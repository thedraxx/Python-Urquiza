from ImcApp import calcular_IMC
from GcApp import calcular_porcentaje_grasa
from TmbApp import calcular_calorias_en_reposo
from Tmb_FisicaApp import calcular_calorias_en_actividad
from ConCalAdelgazar import consumo_calorias_recomendado_para_adelgazar

print('Bienvenido.')
peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))
edad = int(input('Ingrese su edad: '))
genero = input('Ingrese su genero: (F o M) ')
actividadFisica = int(input('Indique grado de actividad realizada: (1) Poco o ninguno, (2) Ejercicio ligero, (1 a 3 dias a la semana), (3) Ejercicio moderado (3 a 5 dias a la semana), (4) Deportista (6 a 7 dias a la semana), (5) Atleta (Entrenamiento manana y tarde) '))
