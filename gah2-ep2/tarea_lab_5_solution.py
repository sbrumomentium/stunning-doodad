def pregunta_1(arboles_inicial: int, arboles_objetivo: int, factor: float) -> int:
    years = 0
    actual = arboles_inicial
    while actual < arboles_objetivo:
        actual = actual * factor
        years += 1
    return years


def pregunta_2(years: int) -> int:
    energia = 0
    for i in range(1, years + 1):
        if i % 5 == 0:
            energia += 30
        elif i % 2 == 0:
            energia += 12
        else:
            energia += 5
    return energia

def pregunta_3(rondas: int, dmg: int) -> int:
    golpes_totales = 0
    for r in range(1, rondas + 1):
        vida = r * 10

        golpes = (vida + dmg - 1) // dmg
        golpes_totales += golpes
    return golpes_totales


def pregunta_4(a: int, b: int, n: int) -> int:
    suma_a = 0
    for i in range(a, n + 1, a):
        suma_a += i
    suma_b = 0
    for i in range(b, n + 1, b):
        suma_b += i

    if suma_a > suma_b:
        return suma_a
    else:
        return suma_b
