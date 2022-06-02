# leer datos
def leer_entero_rango(cartel: str, desde: int, hasta: int) -> int:

    todo_bien = False
    while not todo_bien:
        try:
            entero = int(input(f"{cartel}"))
        except:
            pass
        else:
            if desde <= entero <= hasta:
                todo_bien = True
    return entero


def leer_entero_rango_union(cartel: str, desde: int, hasta: int, union: int) -> int:

    todo_bien = False
    while not todo_bien:
        try:
            entero = int(input(f"{cartel}"))
        except:
            pass
        else:
            if (desde <= entero <= hasta) or (entero == union):
                todo_bien = True
    return entero


def leer_float_rango(cartel: str, desde: float, hasta: float) -> float:

    todo_bien = False
    while not todo_bien:
        try:
            valor_float = float(input(f"{cartel}"))
        except:
            pass
        else:
            if desde <= valor_float <= hasta:
                todo_bien = True
    return valor_float


def leer_float_rango_union(cartel: str, desde: float, hasta: float, union: float) -> float:

    todo_bien = False
    while not todo_bien:
        try:
            valor_float = float(input(f"{cartel}"))
        except:
            pass
        else:
            if (desde <= valor_float <= hasta) or (valor_float == union):
                todo_bien = True
    return valor_float


def leer_tiempo_prueba(dia: int) -> int:
    """
    Ingresa el tiempo de la prueba 
    """
    todo_bien = False
    print("Dia ", dia + 1)
    while not todo_bien:
        try:
            tiempo_prueba = leer_entero_rango(
            "Tiempo de prueba:", 1, 99)
        except:
            pass
        else:
            todo_bien = True
    return tiempo_prueba


# Tiempo de Pruebas
def maxT(tiempo_prueba_lista: list) -> bool:
    mayor = max(tiempo_prueba_lista)
    return print("El mayor tiempo que hizo el atleta fue de: ", mayor ,"minutos")


def totalP(tiempo_prueba_lista: list) -> bool:
    prom = sum(tiempo_prueba_lista)/len(tiempo_prueba_lista) 
    return print("El promedio total es de: ", prom ,"minutos")

def minT(tiempo_prueba_lista: list) -> bool:
    menor = min(tiempo_prueba_lista)
    return print("El menor tiempo que hizo el atleta fue de: ", menor ,"minutos")


# Dias de pruebas por defecto
DIAS_ENTRENAMIENTO = int(10)

# Validaciones
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
    Si al menos una prueba, su tiempo es menor que 15 minutos; entonces, retorna True.\n
    Si no, retorna False, por ende, no es apto para la prueba de 5km

    [False,True;False] ==> True

    """

    tiempo_valido = any(tiempo < 15 for tiempo in tiempo_prueba_lista)

    return tiempo_valido


def validar_condicion_3(tiempo_prueba_lista: list) -> bool:
    """
    Si el promedio de los tiempos es menor o igual a 18 minutos, retorna True.\n
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


# Informa Condicion
def informar_aptitud(es_apto: bool) -> None:

    print("*"*100)
    print("Informar".center(100))
    if es_apto:
        print("El atleta es apto para la prueba de 5km")
    else:
        print("El atleta no es apto para la prueba de 5km")

