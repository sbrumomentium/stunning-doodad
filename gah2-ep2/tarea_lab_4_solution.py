def pregunta_1(agua: float) -> int:
    minutos = 0
    contenido = agua

    while contenido > 0:
        contenido = contenido - 1.0 - (contenido / 3.0)
        minutos += 1

    return minutos


def pregunta_2(energia: float, horas: int) -> float:
    energia_restante = energia

    for h in range(1, horas + 1):
        if 1 <= h <= 3:
            energia_restante -= 0.05 * energia
        elif 4 <= h <= 7:
            energia_restante -= 0.10 * energia
        else:
            energia_restante -= 0.20 * energia

    return round(energia_restante, 4)

def pregunta_3(rondas: int, danio: int) -> int:
    total_golpes = 0

    for r in range(1, rondas + 1):
        vida_jefe = r * 10

        golpes_ronda = (vida_jefe + danio - 1) // danio
        total_golpes += golpes_ronda

    return total_golpes


def pregunta_4(a: float, b: float, c: float) -> float:
    if (a < b + c) and (b < c + a) and (c < a + b):
        s = (a + b + c) / 2.0
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return round(area, 2)
    else:
        return 0.0
