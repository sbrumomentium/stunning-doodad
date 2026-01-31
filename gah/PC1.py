from math import pi, sqrt


def pregunta_1(a: float, b: float) -> float:
    """
    Parametros:
        a (float): semieje mayor de la elipse
        b (float): semieje menor de la elipse
    Retorna:
        float: el perimetro aproximado, redondeado a dos decimales
    """
    valor = pi * (3 * (a + b) - sqrt((3 * a + b) * (a + 3 * b)))

    return round(valor, 2)


print(pregunta_1(3, 2))


def pregunta_2(temp: int) -> str:
    """
    Parametros:
        temp (int): Temperatura en grados Celsius.
    Retorna:
        str :  Descripcion del clima
    """
    if temp < 0:
        return "Congelado"
    elif 0 <= temp <= 10:
        return "Muy frio"
    elif 11 <= temp <= 20:
        return "Frio"
    elif 21 <= temp <= 30:
        return "Templado"
    else:
        return "Caluroso"


print(pregunta_2(-5))
print(pregunta_2(8))
print(pregunta_2(20))
print(pregunta_2(35))


def pregunta_3(deuda: int, pago: int) -> int:
    """
    Parametros:
        deuda (int): monto inicial de la deuda
        pago (int): pago fijo mensual
    Retorna:
        int : la cantidad de meses necesarios para pagar la deuda
    """
    contador = 0
    while deuda > 0:
        deuda = deuda - pago
        contador += 1

    return contador


print(pregunta_3(1000, 200))


def pregunta_4(inicio: int, fin: int) -> int:
    """
    Parametros:
        inicio (int): inicio del rango
        fin (int): fin del rango
    Retorna:
        int : cantidad de multiplos de 4 en el rango
    """
    contador = 0
    i = inicio
    while i <= fin:
        if i % 4 == 0:
            contador += 1
        i += 1
    return contador


print(pregunta_4(1, 10))
