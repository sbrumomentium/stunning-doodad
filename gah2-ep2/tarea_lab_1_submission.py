from math import pi,sqrt


def pregunta_1(radio: float, angulo: float) -> float:
    longitud = radio * angulo * (pi / 180)
    return round(longitud, 2)



def pregunta_2(vx: float, vy: float, vz: float) -> float:
    """
    Parametros:
        vx (float):  Es la coordenada en x
        vy (float):  Es la coordenada en y
        vz (float):  Es la coordenada en z
    Retorna:
        float : es el modulo
    """
    modulo = sqrt(vx ** 2 + vy ** 2 + vz ** 2)
    return round(modulo, 2)



def pregunta_3(edad: int) -> str:
    """
    Parametros:
        edad (int): Edad de la persona.
    Retorna:
        str: Clasificacion de la edad.
    """
    if edad < 13:
        return "Menor"
    elif 13 <= edad < 18:
        return "Adolescente"
    elif 18 <= edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"

def pregunta_4(peso: int, altura: float) -> str:
    """
    Parametros:
      peso (float): Peso en kilogramos (kg).
      altura (float): Altura en metros (m).
    Retorna:
        str : La categoria del IMC segun la OMS.
    """
    imc = peso / (altura * altura)

    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
