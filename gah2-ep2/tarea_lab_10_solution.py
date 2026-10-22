def pregunta_1(matriz: list[list]) -> tuple[list, list]:
    """
    Parametros:
        matriz  (list[list[str]]) : El mapa
    Retorna:
        (list,list) : Una tupla de dos listas
    """
    if not matriz or not matriz[0]:
        return [], []

    max_filas = [max(fila) for fila in matriz]
    max_columnas = [max(matriz[i][j] for i in range(len(matriz))) for j in range(len(matriz[0]))]

    return (max_filas, max_columnas)


def pregunta_2(matriz: list[list[int]]) -> list[list[int]]:
    """
    Parametros:
        matriz (List[List[int]]): La matriz cuadrada a rotar.
    Retorna:
        List[List[int]]: Una nueva matriz rotada 90 grados en sentido horario.
    """
    n = len(matriz)
    matriz_rotada = []

    for i in range(n):
        nueva_fila = []
        for j in range(n):

            nueva_fila.append(matriz[n - 1 - j][i])
        matriz_rotada.append(nueva_fila)

    return matriz_rotada


def pregunta_3(a: list[int], b: list[int], c: list[int]) -> list[list[int]]:
    """
    Parametros:
		a (list[int]): elementos de la diagonal principal.
		b (list[int]): elementos de la diagonal superior.
		c (list[int]): elementos de la diagonal inferior.
    Retorna:
    list[list[int]]: matriz tridiagonal
    """
    n = len(a)
    matriz_tridiagonal = [[0] * n for _ in range(n)]

    for i in range(n):

        matriz_tridiagonal[i][i] = a[i]


        if i < n - 1:
            matriz_tridiagonal[i][i + 1] = b[i]
            matriz_tridiagonal[i + 1][i] = c[i]

    return matriz_tridiagonal


def pregunta_4(matriz: list[list[int]]) -> list[int]:
    """
    Parametros:
        matriz (list[list[int]]): Matriz de enteros (m x n).
    Retorna:
        list[int]: Lista con los indices de filas que contienen el patron.
    """
    indices_encontrados = []

    for i in range(len(matriz)):
        fila = matriz[i]

        for j in range(len(fila) - 2):
            if fila[j] == 1 and fila[j + 1] == 2 and fila[j + 2] == 3:
                indices_encontrados.append(i)
                break

    return indices_encontrados