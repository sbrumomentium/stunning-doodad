from operator import truediv


def pregunta_1(fiebre: bool, dolor_cabeza: bool, ayuno: bool):

    if fiebre == True:
        resultado = True
        return resultado
    else:
        if dolor_cabeza == True and ayuno == True:
            resultado = True
            return resultado
        else: resultado = False
    return resultado
print(pregunta_1(False, False, False))

def pregunta_2(humedad:int)-> str:
    # humedad = int(input("Cual es el porcentaje de humedad: "))
    # if humedad < 30 : categoria = "Ambiente Seco"
    # if 30 <= humedad < 60 : categoria = "Humedad Moderada"
    # if 60 <= humedad < 80 : categoria = "Humedo"
    # if 80 <= humedad < 100 : categoria = "Muy Humedo"
    if humedad < 30 : categoria = "Ambiente seco"
    else:
        if humedad <= 59: categoria = "Humedad moderada"
        else:
            if humedad <= 79: categoria = "Humedo"
            else: categoria = "Muy humedo"
    return categoria

print(pregunta_2(90))
def pregunta_3(saldo_inicial: float, meses: int) ->float:
    while True:
        saldo_nuevo = saldo_inicial * (1+0.02)
        meses = meses - 1
        saldo_inicial = saldo_nuevo
        if meses == 0:

            break

    return round (saldo_nuevo, 2)
print(pregunta_3(95, 2))
def pregunta_4(num:int)->int:
    i = 1
    suma = 0
    while i <= num:
        suma = suma + (i ** 2)
        i = i + 2
    return suma

print(pregunta_4(7))