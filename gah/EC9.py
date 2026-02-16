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
def bubble_sort(lista):
 for tope in range(len(lista)-1, 0, -1):
   for i in range(tope):
     if lista[i] > lista[i+1] :
       temp = lista[i]
       lista[i] = lista[i+1]
       lista[i+1] = temp
def bubble_sort_p4(lista):
    for tope in range(len(lista) - 1, 0, -1):
        for i in range(tope):
            if lista[i]["nota"] < lista[i + 1]["nota"]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
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
    nueva_carta = carta

    for i in range(len(productos)):
        producto = productos[i]
        precio = nuevos_precios[i]


        if producto in nueva_carta:
            nueva_carta[producto] = precio

    return nueva_carta



def pregunta_2(magos: list[dict]) -> list[str]:
    """
    Parametros:
        magos (list[dict]): Lista de diccionarios con informacion de magos.
    Retorna:
        list[str]: Lista con los nombres de los magos aprobados, ordenados alfabeticamente.
    """
    aprobados = linear_search(magos,"aprobado")
    bubble_sort(aprobados)
    return aprobados


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
    generos_unicos = []
    for libro in libros:
        genero = libro['genero']
        if genero not in generos_unicos:
            generos_unicos.append(genero)


    bubble_sort(generos_unicos)

    return generos_unicos


def pregunta_4(estudiantes: list[dict], umbral: float) -> list[dict]:
    """
    Parametros:
        estudiantes (list[dict]): Lista de diccionarios con claves 'nombre' y 'nota'.
        umbral (float): Nota minima aprobatoria.
    Retorna:
        list[dict]: Lista de estudiantes aprobados ordenada de mayor a menor nota.
    """
    lista_de_aprobados = []
    for elem in estudiantes:
        if elem["nota"] >= umbral:
            lista_de_aprobados.append(elem)
    bubble_sort_p4(lista_de_aprobados)
    return lista_de_aprobados