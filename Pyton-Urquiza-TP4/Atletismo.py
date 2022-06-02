# Aca se llama a las funciones
import modulo_funciones_basicas as mod_bac
from TotalPruebas import totalP
from Prueba_MasTiempo import maxT
from Prueba_MenosTiempo import minT

# CONSTANTES
DIAS_ENTRENAMIENTO = int(10)

# FUNCIONES


def leer_tiempo_prueba(dia: int) -> int:
    """
    Ingresa el tiempo de la prueba 
    """
    todo_bien = False
    print("Dia ", dia + 1)
    while not todo_bien:
        try:
            tiempo_prueba = mod_bac.leer_entero_rango(
                "Tiempo de prueba:", 1, 99)
        except:
            pass
        else:
            todo_bien = True
    return tiempo_prueba


def validar_condicion_1(tiempo_prueba_lista: list) -> bool:
    """
    Si ningun tiempo es mayor  a 20 minutos, entonces es apto y retorna True.\n
    Si no, no es apto y retorna False

     [False,True;False] ==> False
    """
    tiempo_valido = all(tiempo <= 20 for tiempo in tiempo_prueba_lista)

    return tiempo_valido


def validar_condicion_2(tiempo_prueba_lista: list) -> bool:
    """
    Si al menos una prueba, su tiempo es menor que 15m; entonces, retorna True.\n
    Si no, retorna False, por ende, no es apto para la prueba de 5km

    [False,True;False] ==> True

    """

    tiempo_valido = any(tiempo < 15 for tiempo in tiempo_prueba_lista)

    return tiempo_valido


def validar_condicion_3(tiempo_prueba_lista: list) -> bool:
    """
    Si el promedio de los tiempos es menor o igual a 18, retorna True.\n
    Si no, retorna False
    """
    promedio_tiempos = float(0)
    for tiempos in tiempo_prueba_lista:
        promedio_tiempos += tiempos
    promedio_tiempos /= len(tiempo_prueba_lista)
    promedio_valido = promedio_tiempos <= 18
    return promedio_valido


def validar_aptitud_atleta(tiempo_prueba_lista: list) -> bool:

    condicion_1 = validar_condicion_1(tiempo_prueba_lista)
    condicion_2 = validar_condicion_2(tiempo_prueba_lista)
    condicion_3 = validar_condicion_3(tiempo_prueba_lista)
    atleta_apto = False
    if condicion_1 and condicion_2 and condicion_3:
        atleta_apto = True
    return atleta_apto


def informar_aptitud(es_apto: bool) -> None:

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

    # Aca se calcula el promedio de las listas
    totalP(tiempo_prueba_lista)
    # Aca se visualiza la prueba que mas se tardo
    maxT(tiempo_prueba_lista)
    # Aca se visualiza la prueba con menos tiempo
    minT(tiempo_prueba_lista)


main()
