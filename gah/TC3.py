def pregunta_1(nombres: list[str]) -> list[str]:
    """
    Parametros:
        nombres (list[str]): lista de nombres como cadenas
    Retorna:
        list[str]: lista de nombres validos en mayusculas
    """
    validos = []
    for nombre in nombres:
            if len(nombre) >= 5 and nombre[0].isupper():
                validos.append(nombre.upper())
    return validos
n=["Juan" , "ana" , "Carlos" , "Bob" , "Eduardo"]
print (pregunta_1 (n))
def pregunta_2(matriz: list[list[int]]) -> str:
    """
    Parametros:
        matriz (list[list[int]]): matriz cuadrada de numeros enteros
    Retorna:
        str: "P" si la diagonal principal es mayor,
             "S" si la diagonal secundaria es mayor,
             "I" si son iguales
    """
    n = len(matriz)
    suma_p = 0
    suma_s = 0

    for i in range(n):
        suma_p += matriz[i][i]
        suma_s += matriz[i][n - 1 - i]

    if suma_p > suma_s:
        return "P"
    elif suma_s > suma_p:
        return "S"
    else:
        return "I"
print(pregunta_2([
[1 , 2 , 3] ,
[4 , 5 , 6] ,
[7 , 8 , 9]]))


def pregunta_3(sucursales: list[dict[str, int]]) -> dict[str, int]:
    """
    Parametros:
        sucursales (list): Lista de diccionarios con inventarios por sucursal.
    Retorna:
        dict: Diccionario con la suma total por producto.
    """
    inventario_total = {}
    for sucursal in sucursales:
        for producto, cantidad in sucursal.items():

            if producto in inventario_total:
                inventario_total[producto] += cantidad
            else:
                inventario_total[producto] = cantidad
    return inventario_total

print(pregunta_3((
{ " laptops " : 5} ,
{ " laptops " : 3} ,
{ " mouse "   : 7} ,
{ " monitor " : 6})))
def pregunta_4(suscripcion: dict, precios: dict) -> float:
    """
    Parametros:
        suscripcion (dict): Actividades y meses contratados.
        precios (dict): Precio mensual de cada actividad.
    Retorna:
        float: Total a pagar, con 20% de descuento si hay 3 o más actividades.
    """
    total = 0.0

    for actividad, meses in suscripcion.items():
        total += meses * precios[actividad]


    if len(suscripcion) >= 3:
        total *= 0.80

    return float(total)
# print(pregunta_4((
# {'yoga' : 3,  'pesas': 2},
# {'yoga' : 40, 'pesas': 50})))