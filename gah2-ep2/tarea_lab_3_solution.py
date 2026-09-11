def pregunta_1(n: float, T: float, V: float, a: float, b: float) -> float:
    R = 8.314
    termino_1 = (n * R * T) / (V - (n * b))
    termino_2 = (a * (n ** 2)) / (V ** 2)
    presion = termino_1 - termino_2
    return round(presion, 3)

def pregunta_2(cantidad: int, precio: float) -> float:
    if cantidad > 100:
        descuento = 25
    elif 50 < cantidad <= 100:
        descuento = 18
    elif 20 <= cantidad <= 50:
        descuento = 10
    elif 10 <= cantidad < 20:
        descuento = 5
    else:
        descuento = 0

    total = cantidad * precio * (1 - (descuento/100))
    return round(total, 2)
# print(pregunta_2(5,10))
# print(pregunta_2(30,15))
# print(pregunta_2(120,8))
# print(pregunta_2(15,20))
# print(pregunta_2(75,10))
def pregunta_3(monedas: int, estrella: bool, vidas: int) -> str:
    mario = bool(True)
    if vidas == 0:
        return "Game Over"

    if estrella:
        if monedas >= 50:
            return "Invencible y Bonus"
        return "Invencible"

        # Casos sin estrella
    if monedas >= 100:
        return "Vida Extra"
    elif monedas >= 50:
        return "Bonus"
    else:
        return "Continuar"

def pregunta_4(cafeina: float) -> int:
    horas = 0
    nivel_actual = cafeina

    while nivel_actual >= 20.0:
        nivel_actual /= 2.0
        horas += 1

    return horas
