from math import sqrt

def calcular_distanca(x1, y1, x2, y2):
    dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

#x_1 = 3
#y_1 = 4
#x_2 = 7
#y_2 = 8
#distancia = calcular distancia (x_1, y_1, x_2, y_2)
print(calcular_distanca(1, 2, 3, 4))

def sumarDigitos (num):
    d1 = num %   10
    num = num // 10
    d2 = num %   10
    num = num // 10
    d3 = num %   10
    num = num // 10
    d4 = num %   10
    num = num // 10
    suma = d1 + d2 + d3 + d4
    return suma
numero = int(input("Ingrese un numero de 4 digitos: "))
suma = sumarDigitos(numero)
print("Suma es: ", suma)

def par_impar (numa):
    if numa % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"
numinput = int(input("Ingrese un numero que sea par o impar: "))
respuesta = par_impar(numinput)
print(respuesta)

def par_impar_zero (nume)
    if nume > 0:
        return "El numero es par"
    elif nume < 0:
        return "El numero es impar"
    else:
        return "El numero es cero"
numamput = int (input("Ingrese un numero que sea: "))
resultado = par_impar_zero(numamput)
print(resultado)
