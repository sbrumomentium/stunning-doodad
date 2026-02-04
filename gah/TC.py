def pregunta_1(n: int) -> str:
    """
    Parametros:
        n (int): numero entero.
    Retorna:
        str: cadena de caracteres que tiene el triangulo
    """
    acumulador = ""
    i = 1
    while i <= n:
        j = n

        while j != 0:
            if (j == i) or (n == i) or (j == 1):
                acumulador = acumulador + "*"
            else:
                acumulador = acumulador + " "
            j -= 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador


def pregunta_2(m: float, vf: float, vi: float, t: float) -> float:
    """
    Parametros:
        m (float) : masa
        vf (float) :  velocidad final
        vi (float) :  velocidad inicial
        t (float): tiempo
    Retorna:
        float : la fuerza
    """
    return None


def pregunta_3(secuencia: str) -> str:
    """
    Parametros:
        secuencia (str) : secuencia de adn
    Retorna:
        str : la secuencia modificada
    """
    return None


def pregunta_4(lista: list) -> list:
    """
    Parametros:
        lista (list) : una lista de numeros
    Retorna:
        list : es la lista normalizada
    """
    return None
