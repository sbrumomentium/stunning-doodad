def pregunta_1(l: int, r: int) -> int:
    cantidad_bisiestos = 0
    for anio in range(l, r + 1):
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            cantidad_bisiestos += 1
    return cantidad_bisiestos


def pregunta_2(longitud_total: float, longitud_rollo: float) -> int:
    total_rollos = 0
    while (longitud_total - longitud_rollo) >= 5.0:
        total_rollos += 1
        longitud_total -= longitud_rollo
    return total_rollos

def pregunta_3(cantidad_aviones: int, vuelos_por_avion: int) -> float:
    costo_total = 0.0
    for avion in range(1, cantidad_aviones + 1):
        costo_vuelo_actual = 5000.0 + (125.50 * avion)
        for vuelo in range(1, vuelos_por_avion + 1):
            costo_total += costo_vuelo_actual
            if vuelo % 40 == 0:
                costo_total += 20500.50
    return round(costo_total, 1)

def pregunta_4(N: int) -> tuple[int, int]:
    suma_pares = 0
    suma_impares = 0
    for digito in str(N):
        valor = int(digito)
        if valor % 2 == 0:
            suma_pares += valor
        else:
            suma_impares += valor
    return (suma_pares, suma_impares)
