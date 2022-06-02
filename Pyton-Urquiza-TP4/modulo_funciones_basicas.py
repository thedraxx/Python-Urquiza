

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
