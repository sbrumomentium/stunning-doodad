def linear_search(lista, e):
    lista_vacia= []
    for i in range(0,len(lista)):
        if lista[i]["calificacion"] == e:
            lista_vacia.append(lista[i]["nombre"])
    return lista_vacia
def linear_search_preg1(lista,e,nuevo_precio):
    for elem in lista.keys():
        if elem == e:
            lista[elem]=nuevo_precio
    return lista

def pregunta_1(
    carta: dict[str, float], productos: list[str], nuevos_precios: list[float]
) -> dict[str, float]:
    """
    Parametros:
        carta (dict): {nombre_producto: precio_en_soles}
        productos (list): lista de nombres de productos a actualizar
        nuevos_precios (list): lista con los nuevos precios

    Retorna:
        dict: {nombre_producto: precio_actualizado_en_soles}
               Devuelve el diccionario de la carta con los precios actualizados.
    """
    # for i in range (0,len(productos)):
    #
    # return None


def pregunta_2(magos: list[dict]) -> list[str]:
    """
    Parametros:
        magos (list[dict]): Lista de diccionarios con informacion de magos.
    Retorna:
        list[str]: Lista con los nombres de los magos aprobados, ordenados alfabeticamente.
    """
    aprobados = linear_search(magos,"aprobado")
    alfabeticos =sorted(aprobados)
    return alfabeticos


def pregunta_3(libros: list[dict]) -> list[str]:
    """
    Parametros:
        libros (list[dict]): Lista de diccionarios. Cada diccionario
                             representa un libro con las claves
                             'titulo', 'autor', 'anio' y 'genero'.
    Retorna:
        list[str]: Lista de generos sin repetir, ordenados
                   alfabeticamente usando Bubble Sort.
    """
    return None


def pregunta_4(estudiantes: list[dict], umbral: float) -> list[dict]:
    """
    Parametros:
        estudiantes (list[dict]): Lista de diccionarios con claves 'nombre' y 'nota'.
        umbral (float): Nota minima aprobatoria.
    Retorna:
        list[dict]: Lista de estudiantes aprobados ordenada de mayor a menor nota.
    """
    return None