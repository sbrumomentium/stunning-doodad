def pregunta_1(x: int, y: int, z: int) -> int:
    # Tu código aquí. Recuerda retornar el resultado.
    resultado = ((x ** 2 + y ** 2) // z) + (x*y)%z
    return  resultado

print (pregunta_1(5,3,2))

def pregunta_2(a: int, b: int, c: int) -> str:
    # Tu código aquí. Recuerda retornar el resultado.
    if (a+b)>c and b+c>a and c+a>b:
        if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
            return "Escaleno rectangulo"
        elif a == b == c:
            return "Equilatero"
        elif a==b or b==c or c==a:
            return "Isosceles"
        # elif a!=b and b!=c and c!=a:
        else:
            return "Escaleno"
    else: return "No es triangulo"
print(pregunta_2(3, 4,5))

def pregunta_3(n: int) -> int:
    # Tu código aquí. Recuerda retornar el resultado.
    suma = 0

    while n > 0:
        if n % 3 == 0 or n % 5 == 0:
        # if n % 15 == 0:
            suma = suma + n
        n -= 1
    return suma
print(pregunta_3(10))
def pregunta_4(n: int) -> int:
    acumulador = ""
    i = 1

    while i <= n:
        j = 1
        while j <= i:
            acumulador = acumulador + str("*")
            j += 1
        i += 1
        if i <= n:
            acumulador = acumulador + "\n"
    return acumulador
print(pregunta_4(3))