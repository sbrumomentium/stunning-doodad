from math import sqrt


def pregunta_1(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Parametros:
        x1 (float): coordenada x del primer punto
        y1 (float): coordenada y del primer punto
        x2 (float): coordenada x del segundo punto
        y2 (float): coordenada y del segundo punto

    Retorna:
        float: pendiente de la recta redondeada a 2 decimales
    """
    m=(y2-y1)/(x2-x1)
    return round(m,2)
print(pregunta_1(2, 3, 5, 11))

def pregunta_2(humedad: int) -> str:
    """
    Parametros:
        humedad (int): porcentaje de humedad ambiental

    Retorna:
        str: categoria
    """
    if humedad < 30:
        return "Ambiente seco"
    elif humedad <= 59:
        return "Humedad moderada"
    elif humedad <=79:
        return "Humedo"
    else:
        return "Muy humedo"



print(pregunta_2(29))


def pregunta_3(deuda: int, pago: int) -> int:
    """
    Parametros:
        deuda (int): monto inicial de la deuda
        pago (int): pago fijo mensual

    Retorna:
        int: la cantidad de meses necesarios para pagar la deuda
    """
    meses = 0
    while deuda > 0:
        deuda = deuda - pago
        meses += 1
    return meses

print(pregunta_3(1000,200))
def pregunta_4(numero: int) -> float:
    """
    Parametros:
        numero (int): Es un numero entero

    Retorna:
        float: numero redondeado a 3 decimales
    """
    i = 1
    suma = 1
    while i <= numero:

        if i % 2 == 0:
            suma = suma * sqrt(i)
        i = i + 1
    return round(suma,3)
print(pregunta_4(7))



