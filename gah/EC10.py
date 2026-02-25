
def bubble_sort(lista):
 for tope in range(len(lista)-1, 0, -1):
   for i in range(tope):
     if lista[i] > lista[i+1] :
       temp = lista[i]
       lista[i] = lista[i+1]
       lista[i+1] = temp

def pregunta_1(rendimiento: dict) -> dict:
    """
    Parametros:
        rendimiento (dict): Diccionario con los nombres de empleados como claves y una lista de enteros representando sus puntuaciones.
    Retorna:
        dict: Diccionario con los nombres de empleados y su promedio de rendimiento.
    """
    nuevo_rendimiento = {}
    for empleado, puntuaciones in rendimiento.items():
        if len(puntuaciones) > 0:
            promedio = sum(puntuaciones) / len(puntuaciones)

            nuevo_rendimiento[empleado] = round(promedio, 2)
        else:
            nuevo_rendimiento[empleado] = 0.0
    return nuevo_rendimiento


def pregunta_2(lista_paises:list[dict], pais_objetivo:str)->float:
    """
    Parametros:
        lista_paises(list[dict]) : La lista de diccionarios
        pais_objetivo (str) : El nombre del pais a buscar
    Retorna:
        (float) : el valor del crecimiento
    """
    n = len(lista_paises)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_paises[j]['pais'].lower() > lista_paises[j+1]['pais'].lower():
                lista_paises[j], lista_paises[j+1] = lista_paises[j+1], lista_paises[j]


    bajo = 0
    alto = len(lista_paises) - 1
    objetivo = pais_objetivo.lower()

    while bajo <= alto:
        medio = (bajo + alto) // 2

        nombre_actual = lista_paises[medio]['pais'].lower()

        if nombre_actual == objetivo:
            return float(lista_paises[medio]['crecimiento'])
        elif nombre_actual < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1


    return 0.0


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
    lista_generos = []
    for elem in libros:
        if elem["genero"] not in lista_generos:
            lista_generos.append(elem["genero"])
    bubble_sort(lista_generos)
    return lista_generos


def pregunta_4(lista: list[dict]) -> list[dict]:
    """
    Parametros:
    	lista (list[dict]) :  lista de diccionarios
    Retorna:
    	list[dict] : lista de diccionarios
    """
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            total_actual = lista[j]['oro'] + lista[j]['plata']
            total_siguiente = lista[j + 1]['oro'] + lista[j + 1]['plata']

            if total_actual < total_siguiente:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
