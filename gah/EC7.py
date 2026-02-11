def pregunta_1(nombres: list[str], niveles: list[int], minimo: int) -> list[str]:
    """
    Parametros:
        nombres (list[str]): lista de nombres de los candidatos
        niveles (list[int]): lista de niveles correspondientes
        minimo (int): nivel minimo requerido
    Retorna:
        list[str]: lista con los nombres que cumplen con el requisito
    """
    seleccionados = []
    for i in range(len(nombres)):
        if niveles[i] >= minimo:
            seleccionados.append(nombres[i])
    return seleccionados


def pregunta_2(sprite: list[list[str]]) -> list[list[str]]:
    """
    Parametros:
        sprite (list[list[str]]): matriz de caracteres que representa el sprite
    Retorna:
        list[list[str]]: nueva matriz con el sprite reflejado horizontalmente
    """
    matriz_reflejada = []
    for fila in sprite:

        fila_invertida = fila[::-1]
        matriz_reflejada.append(fila_invertida)
    return matriz_reflejada


def pregunta_3(suscripcion: dict, precios: dict) -> float:
    """
    Parametros:
        suscripcion (dict): Actividades y meses contratados.
        precios (dict): Precio mensual de cada actividad.
    Retorna:
        float: Total a pagar, con 20% de descuento si hay 3 o mas actividades.
    """
    costo_total = 0.0

    for actividad, meses in suscripcion.items():
        costo_total += meses * precios[actividad]


    if len(suscripcion) >= 3:
        costo_total *= 0.80

    return costo_total


def pregunta_4(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """
    Parametros:
        A (list[list[int]]) :  primer bloque
        B (list[list[int]]) :  segundo bloque
    Retorna:
        list[list[int]] : matriz diagonal por bloques
    """
    n = len(A)
    m = len(B)
    dimension_total = n + m

    matriz_bloques = [[0 for _ in range(dimension_total)] for _ in range(dimension_total)]


    for i in range(n):
        for j in range(n):
            matriz_bloques[i][j] = A[i][j]


    for i in range(m):
        for j in range(m):
            matriz_bloques[i + n][j + n] = B[i][j]

    return matriz_bloques