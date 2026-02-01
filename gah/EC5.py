
def pregunta_1(num1: int, num2: int, multiplo: int) ->int:
    """
    Retorna la cantidad de sumas de x y de y que sean multiplos del parametro multiplo
    Parametros:
        num1 (int) : representa el menor valor de x y de y
        num2 (int) : representa el mayor valor de x y de y
        multiplo (int) : representa el multiplo a evaluar
    Retorna:
        int : la cantidad de multiplos que hay
    """
    contador = 0

    for x in range(num1, num2 + 1):

        for y in range(num1, num2 + 1):
            suma = x + y

            if suma % multiplo == 0:
                contador += 1
    return contador

def pregunta_2(n : int) -> str:
    """
    Parametros:
        n (int) :  numero entero
    Retorna:
        str : cadena de numeros que no tienen el digito 2
    """
    resultado = ""
    for i in range(1, n + 1):

        if '2' not in str(i):

            resultado += str(i) + " "
    return resultado

def pregunta_3(frase : str) -> tuple[int,int]:
    """
    Parametros:
        frase (string) : Una oracion o frase donde cada palabra esta separada por espacios
    Retorna:
        Tuple[int,int] : El primer valor es la cantidad de palabras en la frase. El segundo valor es la cantidad de letras en la frase.
    """

    palabras_lista = frase.split()
    cantidad_palabras = len(palabras_lista)


    cantidad_letras = 0
    for caracter in frase:
        if caracter != ' ':
            cantidad_letras += 1

    return (cantidad_palabras, cantidad_letras)

def pregunta_4(n : int, nota_inicial : int) -> tuple[int, float]:
    """
    Parametros:
        n (int) : Cantidad total de notas a evaluar
        nota_inicial (int) : Valor de la primera nota
    Retorna:
        Tuple[int, float] : El primer valor es la cantidad de notas mayores o iguales a 14.
                            El segundo valor es el promedio de todas las notas generadas, redondeado a 2 decimales.
    """
    contador_aprobados = 0
    suma_total = 0
    nota_actual = nota_inicial

    for _ in range(n):

        suma_total += nota_actual


        if nota_actual >= 14:
            contador_aprobados += 1


        nota_actual += 1


    promedio = 0.0
    if n > 0:
        promedio = round(suma_total / n, 2)

    return (contador_aprobados, promedio)
print(pregunta_1(5,8,7))
print(pregunta_2(4))
print(pregunta_3("Hola Mundo"))
print(pregunta_4(5,12))