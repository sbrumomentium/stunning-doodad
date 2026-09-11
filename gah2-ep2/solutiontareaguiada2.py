from math import log
def pregunta_1(I: float) -> float:
    loud = 10*log(I/10**-12,10)
    return round(loud,3)
# print(pregunta_1(0.15))
# print(pregunta_1(0.025))
def pregunta_2(re: float) -> str:
    if re < 2000:
        return "Laminar"
    elif 2000 <= re <= 4000:
        return "Transicional"
    else:
        return "Turbulento"
# print(pregunta_2(1500))
# print(pregunta_2(3000))
# print(pregunta_2(5000))
def pregunta_3(presion_entrada: float, presion_vapor: float) -> str:
    margen = presion_entrada-presion_vapor
    if margen < 2:
        return "Cavitacion severa"
    elif 2 <= margen < 5:
        return "Riesgo de cavitacion"
    else:
        return "Operacion estable"
print(pregunta_3(8,7))
print(pregunta_3(10,6.5))
print(pregunta_3(14,6))
def pregunta_4(N: float, lam: float, umbral: float) -> int:
    itera = 0
    while N > umbral:
        N = N * (1-lam)
        itera = itera + 1

    return itera

print(pregunta_4(1000,0.2,100))
print(pregunta_4(500,0.1,50))
print(pregunta_4(50,0.1,50))