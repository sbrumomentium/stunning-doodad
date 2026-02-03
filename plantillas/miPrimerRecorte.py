



def pregunta_1(unaLista):
    #retornar los 2 primeros elementos de la lista
    return unaLista[0:2]

def pregunta_2(unaLista):
    # retornar una lista con el primer y último elemento de la lista
    otraLista = []
    otraLista.append(unaLista[0])
    otraLista.append(unaLista[-1])
    return otraLista


def pregunta_3(unaLista):
    # retornar una lista con los elementos impares
    respuesta = []
    for elem in unaLista:
        if elem%2 == 1:
            respuesta.append(elem)
    return respuesta

notas = [20, 18, 19, 18, 20, 17, 20, 3, 8]
y = pregunta_3(notas)
print(y)
def pregunta_4(unaCadena):
# retornar la palabra más larga
    miLista = unaCadena.split()
    lamaslarga = miLista[0]
    for elem in miLista:
        if len(elem)>len(lamaslarga):
            lamaslarga = elem
    return lamaslarga
cadena = "quiero aprobar el curso"
y = pregunta_4(cadena)
print(y)
