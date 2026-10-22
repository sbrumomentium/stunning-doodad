# datos = {"USD":3.86,
#          "EUR":4.10,
#          "GBP":4.71,
#          "JPY":0.026}
# for clave in datos:
#     print(clave,datos[clave])
# for clave in datos.keys():
#     print(clave,datos[clave])
# for valor in datos.values():
#     print(valor)
# for clave, valor in datos.items():
#     print(clave,valor)
# cantidad = int(input("Cantidad: "))
# moneda = input("Moneda: ")
#
# if moneda in datos.keys():
#     conversion = datos[moneda] * cantidad
#     print("equivale a :", conversion)
# else:
#     print("No hay moneda")
#
def pregunta_1(edades:list)->dict:
    dic_cat = {'ninos':0,'adolescentes':0}
    for edad in edades:
        if 0 <= edad <= 12:
            dic_cat['ninos'] += 1
        elif 12 < edad <= 17:
            dic_cat['adolescentes'] += 1
    return dic_cat
lista = [2,6,7,13,16]
dic_cat = pregunta_1(lista)
print(dic_cat)
