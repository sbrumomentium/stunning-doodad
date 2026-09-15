def pregunta_1(horas_redes: float, horas_juegos: float, brillo: float) -> float:
    bateria_final = 100 - ((horas_redes * 12) + (horas_juegos * 20)) * ((brillo / 10) ** 2)
    return round(bateria_final, 2)


def pregunta_2(nivel: int, pm: int, escudo: bool) -> str:
    if nivel >= 50 and pm >= 80 and escudo:
        return "Ataque Lumina"
    elif nivel >= 30 and pm >= 50:
        return "Ataque Especial"
    elif pm >= 20:
        return "Ataque Basico"
    else:
        return "Descansar"

def pregunta_3(consultas_previas: int, precio: float) -> float:
    if consultas_previas >= 8 and precio > 100:
        descuento = 0.30
    elif consultas_previas >= 8 and precio <= 100:
        descuento = 0.20
    elif 4 <= consultas_previas < 8 and precio > 80:
        descuento = 0.15
    elif 4 <= consultas_previas < 8 and precio <= 80:
        descuento = 0.10
    else:
        descuento = 0.0

    monto_final = precio * (1 - descuento)
    return round(monto_final, 2)


def pregunta_4(combustible: float, consumo: float) -> int:
    horas = 0
    while combustible > 0:
        combustible -= consumo
        horas += 1
    return horas