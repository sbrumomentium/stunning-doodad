
from re import split


def pregunta_1(n: int) -> str:
    acumulador = ""
    i = 1
    while i <= n:
        j = n

        while j !=0:
            if  (j==i) or (n==i) or (j==1):
                acumulador = acumulador + "*"
            else:
                acumulador = acumulador + " "
            j -= 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_1(7))
def pregunta_2(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """
    Parametros:
        valor(float) : cantidad a convertir
        unidad_origen(str)  : unidad de medida de origen
        unidad_destino(str) : unidad de medida de destino
    Retorna:
        float : el valor convertido
    """
    valor_origen = valor

    if unidad_origen == "mi" and unidad_destino == "m":
        valor = valor*1609.34
    if unidad_origen == "mi" and unidad_destino == "km":
        valor = valor*1.60934
    if unidad_origen == "km" and unidad_destino == "m":
        valor = valor*1000
    if unidad_origen == "m" and unidad_destino == "km":
        valor = valor/1000
    if unidad_origen == "km" and unidad_destino == "mi":
        valor = valor/1.60934
    if unidad_origen == "m" and unidad_destino == "mi":
        valor = valor/1609.34
    return round(valor, 4)
print(pregunta_2(5, "mi", "km"))

def pregunta_3(nombre: str) -> str:
    """
    Parametros:
         nombre (str): Nombre completo de la persona.
    Retorna:
        str: Iniciales en mayusculas separadas por puntos,
             o 'ERROR' si el nombre tiene menos de dos palabras.
    """
    # acumulador = ""
    # iniciales = ""
    # partes = nombre.strip().split()
    # if len(partes) < 2:
    #     return "ERROR"
    # iniciales = [nombre[0].upper() for nombre in partes]
    # nombre[0].upper() for nombre in partes
    # # acumulador = acumulador + str(iniciales) + "."
    # return iniciales
    # letra = nombre[0]
    # acumulador = ""
    # contador_palabras = 0
    #
    # for i in range (1, len(nombre)):
    #     letra = nombre[i]
    #     if letra == " ":
    #         contador_palabras += 1
    #         for j in range (contador_palabras):
    #
    #             acumulador = acumulador + nombre[0] + "."
    #
    #
    #
    #         return acumulador
    #
    # return "ERROR"
    listaDeNombres = nombre.split()
    if len(listaDeNombres) < 2:
        return "ERROR"
    else:
        cadena = ""
        for elem in listaDeNombres:
            cadena = cadena + elem[0] + "."
        return cadena[0:-1]
print(pregunta_3("JuanCarlosMatias"))
def pregunta_4(stock: list) -> int:
    """
    Parametros:
        stock (list): Lista con las cantidades disponibles de productos
    Retorna:
        int: Cantidad de productos agotados
    """
    respuesta = 0
    for elem in stock:
        if elem == 0:
            respuesta = respuesta + 1
    return respuesta

