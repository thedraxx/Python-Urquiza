import modulo_funciones_basicas as mod_bac


DIAS_ENTRENAMIENTO = int(10)

             
def leer_tiempo_prueba(dia:int) -> int:

    todo_bien = False
    print("Dia ", dia + 1)
    while not todo_bien:
        try:
            tiempo_prueba = mod_bac.leer_entero_rango("Tiempo de prueba:",1,99)
        except:
            pass
        else:
            todo_bien = True
    return tiempo_prueba


def validar_condicion_1(tiempo_prueba_lista:list) -> bool:
 
    tiempo_valido = all(tiempo <= 20 for tiempo in tiempo_prueba_lista)
   
    return tiempo_valido

def validar_condicion_2(tiempo_prueba_lista:list) -> bool:

    tiempo_valido = any(tiempo < 15 for tiempo in tiempo_prueba_lista)

    return tiempo_valido

def validar_condicion_3(tiempo_prueba_lista:list) -> bool:

    promedio_tiempos = float(0)
    for tiempos in tiempo_prueba_lista:
        promedio_tiempos += tiempos
    promedio_tiempos /= len(tiempo_prueba_lista)
    promedio_valido = promedio_tiempos <= 18
    
    return promedio_valido


def validar_aptitud_atleta(tiempo_prueba_lista:list) -> bool:

    condicion_1 = validar_condicion_1(tiempo_prueba_lista)
    condicion_2 = validar_condicion_2(tiempo_prueba_lista)
    condicion_3 = validar_condicion_3(tiempo_prueba_lista)
    atleta_apto = False
    if condicion_1 and condicion_2 and condicion_3:
        atleta_apto = True
    return atleta_apto

def informar_aptitud(es_apto:bool) -> None:
    
    print("*"*100)
    print("Informar".center(100))
    if es_apto:
        print("El atleta es apto para la prueba de 5km")
    else:
        print("El atleta no es apto para la prueba de 5km")

def main():

    tiempo_prueba_lista = []
    cont_dias = int(0)
    while cont_dias < 10:
        tiempo_prueba_lista.append(leer_tiempo_prueba(cont_dias)) 
        cont_dias += 1
    es_apto = validar_aptitud_atleta(tiempo_prueba_lista)

    informar_aptitud(es_apto)



main()