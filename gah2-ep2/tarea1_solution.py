def pregunta_1(distancia_km: int, ritmo_segundos_km: int, pausa_minutos: int) -> int:
    return None


def pregunta_2(ritmo_segundos_km: int) -> str:
    return None


def pregunta_3(edad: int, kilometros_semana: int) -> str:
    return None


def pregunta_4(distancia_km: int, intervalo_km: int) -> int:
    return None

#def pregunta_1(distancia_km, ritmo_segundos_km, pausa_minutos):
    # Tiempo corriendo más las pausas convertidas a segundos
    return (distancia_km * ritmo_segundos_km) + (pausa_minutos * 60)


#def pregunta_2(ritmo_segundos_km):
    if ritmo_segundos_km <= 240:
        return "Elite"
    elif ritmo_segundos_km <= 300:
        return "Competitivo"
    elif ritmo_segundos_km <= 420:
        return "Recreativo"
    else:
        return "En entrenamiento"


#def pregunta_3(edad, kilometros_semana):
    if edad < 18:
        return "No puede inscribirse: edad insuficiente"
    elif kilometros_semana < 30:
        return "No puede inscribirse: preparación insuficiente"
    else:
        return "Inscripción aprobada"


#def pregunta_4(distancia_km, intervalo_km):
    puntos = 0
    km_actual = intervalo_km

    # Solo cuenta los puntos estrictamente antes de la meta
    while km_actual < distancia_km:
        puntos += 1
        km_actual += intervalo_km

    return puntos