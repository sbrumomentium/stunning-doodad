def pregunta_1(filas : int) -> int:
    """
    Contar cuantas casillas negras tiene un tablero cuadrado compuesto por casillas negras y blancas intercaladas, similar al tablero de ajedrez
    Parametros:
        filas (int): El tamaño de filas y columnas del tablero
    Retorna:
        int: La cantidad de casillas negras en el tablero
    """
    contador = 0
    columnas = filas
    i = 0
    for i in range (0, filas):
        for j in range (0, columnas):
            if (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
                contador += 1
    return contador

# print(pregunta_1(3))
# print(pregunta_1(5))

def pregunta_2(tamanio: int) -> str:
    """
    Crea un tablero parecido al de ajedrez formado con los caracteres "#" y "0" de acuerdo al tamanio ingresado como parametro
    Parametros:
        tamanio (int): El tamanio del tablero a crear
    Retorna:
        str: Un tablero formado con los caracteres "#" y "0" con el tamanio especificado, si el tamanio es menor que 2 se debe de retornar el texto "No se puede formar un tablero"
    """
    acumulador = ""
    columnas = tamanio
    i = 0
    if tamanio < 2:
        return "No se puede formar un tablero"
    for i in range(0, tamanio):
        for j in range(0, columnas):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                acumulador=acumulador+"0"
            else:
                acumulador=acumulador+"#"
        acumulador=acumulador+ "\n"
    return acumulador

# print(pregunta_2(8))
# print(pregunta_2(1))

def pregunta_3(numerico: int) -> str:
    """
    Genera un codigo de barras basado en la cantidad de divisores de cada digito del numero ingresado.
    Parametros:
        numerico (int): Numero entero para generar el codigo de barras.
    Retorna:
        str: Una cadena que representa el codigo de barras "|", dependiendo de su cantidad de divisores.
    """
    acumulador = ""

    cifras = str(numerico)
    for x in cifras:
        contador = 0
        num = int(x)
        for i in range(2,num):
            if num % i == 0:
                contador += 1
        if contador == 0:
            acumulador = acumulador + " "
        else:
            for j in range (0,contador):
                acumulador = acumulador + "|"



    return acumulador
print(pregunta_3(92878308))
def pregunta_4(tam: int) -> str:
    """
    Genere un patron de asteriscos "*" en forma de cuadrado hueco
    Parametros:
        tam (int): El tamanio del cuadrado hueco
    Retorna:
        str: Un cuadrado hueco formado con "*" de acuerdo al tamanio ingresado
    """
    acumulador = ""
    i = 1
    while i <= tam:
        j = 1

        while j <= tam:
            if j == 1 or i == 1 or i == tam or j == tam:
                acumulador = acumulador + "*"
            else:
                acumulador = acumulador + " "
            j += 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_4(5))