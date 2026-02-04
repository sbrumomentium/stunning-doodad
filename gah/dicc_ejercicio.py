datos = {"1225" : "Juan",
         "3456" : "Sandra",
         "5656" : "Fernando",
         "2222" : "Pedro"}
def pregunta_1(personas, DNI):
    claves = list(personas.keys())
    encontre = False
    for elem in claves:
        if elem == DNI:
            encontre = True
    if encontre:
        respuesta = personas[DNI]
    else:
        respuesta = "Persona no encontrada"
    return respuesta
print(pregunta_1(datos, "1225"))

def pregunta_2(oracion):
    frase_min = oracion.lower()
    palabras = frase_min.split()
    dicc={}
    for palabra in palabras:
        claves = list(dicc.keys())
        encontre = False
        for clave in claves:
            if clave == palabra:
                encontre = True
        if encontre:
            dicc[palabra]+=1
        else:
            dicc[palabra]=1
    return dicc
print(pregunta_2("Erre con Guitarra, Erre con Barril, Erre con Mic"))
def pregunta_3(frase):
    palabras = frase.split()
    dic= {}
    for palabra in palabras:
        claves = list(dic.keys())
        encontre = False
        for clave in claves:
            if clave == len(palabra):
                encontre = True
        if encontre:
            if palabra not in dic[len(palabra)]:
                dic[len(palabra)].append(palabra)
        else:
            dic[len(palabra)] = palabra
    return dic
