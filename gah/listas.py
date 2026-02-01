def pregunta_respuesta(unaLista):
    respuesta= []
    for elem in unaLista:
        if elem%2==1:
            respuesta.append(elem)
    return respuesta
notas =[20,18,19,18,20,17,20,3,0]
print(pregunta_respuesta(notas))

