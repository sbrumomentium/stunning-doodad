
def pregunta_1(compras: dict[str, list[float]]) -> dict[str, float]:
    """
    Parámetros:
    compras (dict): diccionario con claves como nombres de clientes y
    valores como listas de montos gastados.

    Retorna:
    dict: nuevo diccionario con el total gastado por cada cliente, en el
    mismo orden que el original.
    """


    return None


def pregunta_2(cartelera: list[list], actor: str) -> str:
    """
    Parámetros:
    cartelera (list[list]): Lista de películas. Cada película es [titulo, [actores]].
    actor (str): Nombre del actor a buscar.

    Retorna:
    str: Título de la primera película que contiene al actor o "Actor no encontrado".
    """
    return None


def pregunta_3(lista: list[dict]) -> list[dict]:
    """
    Parámetros:
    datos (list[dict]): La lista de diccionarios de objetos.

    Retorna:
    list[dict]: La lista de diccionarios de objetos ordenada.
    """

    return None


def pregunta_4(extensiones: dict, archivos: list[str]) -> list:
    """
    Parámetros:
    extensiones (dict): diccionario con extensiones como claves y
    lenguajes como valores.

    archivos (list[str]): lista de nombres de archivos.

    Retorna:
    list: lenguajes asociados a cada archivo (o 'Otro' si no se encuentra).
    """
    extension = []
    respuesta = []
    for elem in archivos:
        extension = "."+elem.split(".")[-1]
    # for clave in extensiones.keys():
    #     if extension == clave:
    #         respuesta.append(extensiones[clave])
    claves = list(extensiones.keys())
    if extension in claves:
        respuesta.append(extensiones[extension])
    else:
        respuesta.append("Otro")
    return respuesta