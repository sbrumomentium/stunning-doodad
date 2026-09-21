def pregunta_1(nivel_inicial_cm: int, aumento_diario_cm: int, dias: int, zonas: int) -> int:
    activaciones = 0
    nivel = nivel_inicial_cm

    for dia in range(dias):
        nivel += aumento_diario_cm
        for z in range(1, zonas + 1):
            umbral = 200 + (z - 1) * 20
            if nivel >= umbral:
                activaciones += 1

    return activaciones


def pregunta_2(nivel_inicial_cm: int, aumento_diario_cm: int, dias: int) -> int:
    dias_vigilancia = 0
    nivel = nivel_inicial_cm

    for dia in range(dias):
        nivel += aumento_diario_cm
        if nivel >= 250:
            dias_vigilancia += 1

    return dias_vigilancia

def pregunta_3(personas: int, capacidad_bote: int, nivel_rio_cm: int) -> int:
    if personas == 0:
        return 0

    capacidad_permitida = capacidad_bote
    if nivel_rio_cm >= 300:
        capacidad_permitida -= 1

    viajes = 0
    personas_restantes = personas

    while personas_restantes > 0:
        personas_restantes -= capacidad_permitida
        viajes += 1

    return viajes


def pregunta_4(dias: int, nivel_inicial_cm: int, lluvia_diaria_mm: int) -> int:
    if lluvia_diaria_mm >= 50:
        aumento = 20
    elif 25 <= lluvia_diaria_mm <= 49:
        aumento = 10
    else:
        aumento = 2

    jornadas_alerta = 0
    nivel = nivel_inicial_cm
    dia_actual = 0

    while dia_actual < dias:
        nivel += aumento
        if nivel >= 250:
            jornadas_alerta += 1
        dia_actual += 1

    return jornadas_alerta