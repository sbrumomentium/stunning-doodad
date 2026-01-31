def pregunta_1(vf: float, vi: float, t: float) -> float:
    """
    Parametros:
        vf (float): velocidad final
        vi (float): velocidad inicial
        t (float): tiempo transcurrido
    Retorna:
        float: la aceleracion
    """
    accel = (vf - vi)/t
    return round(accel,1)

print(pregunta_1(46.1,18.5,2.47))


def pregunta_2(coordenada_x: int, coordenada_y: int) -> str:
    """
    Determina si el punto ingresado se encuentra dentro o fuera del anillo
    retornar
    Parametros:
        coordenada_x (int) : un entero de la coordenada x del punto
        coordenada_y (int) : un entero de la coordenada y del punto
    Retorna:
        str : Dice "ESTA DENTRO" o "NO ESTA DENTRO"
    """
    distancia=(coordenada_x**2+coordenada_y**2)**0.5
    if 4 <= distancia <= 6:
        mensaje = "ESTA DENTRO"
    else:
        mensaje = "NO ESTA DENTRO"
    return mensaje

print(pregunta_2(5,5))
def pregunta_3(numero: int) -> float:
    """
    Parametros:
        numero (int) :  Es un numero entero
    Retorna:
    	float : numero redondeado a 3 decimales,
    """
    return None


def pregunta_4(numero: int, digito: int) -> int:
    """
    Parametros:
        numero (int): Numero entero positivo
        digito (int): Digito entre 0 y 9
    Retorna:
        int: Cantidad de veces que el digito aparece en el numero
    """
    return None
