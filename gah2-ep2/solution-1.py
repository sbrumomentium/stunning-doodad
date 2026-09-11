def pregunta_1(x1: float, x2: float, x3: float) -> float:
    h=(3/((1/x1)+(1/x2)+(1/x3)))


    return round(h,2)


def pregunta_2(peso: float, distancia: float) -> str:
    if peso < 5 and distancia < 50:
        return "Local ligero"
    elif peso >= 5 and distancia < 50:
        return "Local pesado"
    elif peso < 10 and 50 <= distancia < 300:
        return "Regional estandar"
    elif peso >= 10 and 50 <= distancia < 300:
        return "Regional pesado"
    elif peso < 20 and distancia >= 300:
        return "Nacional estandar"
    else:
        return "Nacional pesado"

def pregunta_3(consumo: float, area: float, personas: int) -> str:
    consumo_m2 = consumo / area
    puntaje = 0
    if consumo_m2 < 5:
        puntaje = puntaje + 50
    elif 5 <= consumo_m2 <= 8 :
        puntaje = puntaje + 35
    # if consumo > 8:
    else:
        puntaje = puntaje + 15
    if personas <= 2:
        puntaje = puntaje + 20
    elif personas == 3 or personas == 4:
        puntaje = puntaje + 10
    # if personas > 4:
    else:
        puntaje = puntaje + 5
    if puntaje < 25:
        return "Ineficiente"
    elif 25 <= puntaje < 40:
        return "Regular"
    elif 40 <= puntaje < 60:
        return "Eficiente"
    else:
        return "Muy eficiente"
    # return puntaje
print (pregunta_3(350,50, 2))

def pregunta_4(numero: int) -> int:
    divisor = 2
    while numero % divisor != 0:

        divisor = divisor + 1

    return divisor

# print(pregunta_4(35))
# print(pregunta_4(91))
# print(pregunta_4(17))
