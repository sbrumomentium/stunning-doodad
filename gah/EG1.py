from math import sqrt
def pregunta_1(arista:  float) -> float:
    """
    Halla el area de un cuadrilatero ciclico
    Parametros:
    	arista (float) :  Es la arista
    Retorna:
    	float : el volumen, valor expresado con 3 cifras decimales
    """
    volumen = (15 + 7 * sqrt(5)) / 4 * (arista ** 3)
    return round(volumen, 3)

def pregunta_2(lado1: float, lado2: float, lado3: float, lado4:float) ->float:
    """
    Halla el area de un cuadrilatero ciclico
    Parametros:
    	lado1 (float) :  El primer lado
            lado2 (float) :  El segundo lado
            lado3 (float) :  El tercer lado
            lado4 (float) :  El cuarto lado
    Retorna:
    	float : el area, valor expresado con 3 cifras decimales
    """
    s = (lado1 + lado2 + lado3 + lado4) / 2
    area = sqrt((s - lado1) * (s - lado2) * (s - lado3) * (s - lado4))

    return round(area, 3)

def pregunta_3(numero : int)->str:
    """
    Determina la cantidad de digitos iguales que tiene un numero
    Parametros:
        numero (int) : un entero de 3 digitos
    Retorna:
        Str : Es la cadena que contiene el mensaje
    """
    d1 = numero // 100
    d2 = (numero // 10) % 10
    d3 = numero % 10

    if d1 == d2 and d2 == d3:
        return "Tiene tres digitos iguales"
    elif d1 == d2 or d1 == d3 or d2 == d3:
        return "Tiene solo dos digitos iguales"
    else:
        return "Tiene tres digitos diferentes"



def pregunta_4( rango :  int) -> str:
    """
    Halla la clasificacion de IQ
    Parametros:
    	rango (int) :  Es el rango de IQ
    Retorna:
    	Str :  Es la clasificacion que corresponde segun el rango IQ
    """
    if rango >= 130:
        return "Muy Superior"
    elif 120 <= rango <= 129:
        return "Superior"
    elif 110 <= rango <= 119:
        return "Arriba del Promedio"
    elif 90 <= rango <= 109:
        return "Promedio"
    elif 80 <= rango <= 89:
        return "Abajo del Promedio"
    elif 70 <= rango <= 79:
        return "Inferior"
    else:
        return "Deficiente"
    return ""