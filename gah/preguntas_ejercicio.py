def pregunta_1(num):
    #retornar el doble de la cifra del centro, asumiendo que siempre tiene 3 cifras
    cifras_derecha = num%100
    decena = cifras_derecha//10
    respuesta = 2*decena
    return respuesta
def pregunta_2(num):
    #retornar la cifra menor
    u= num%10
    c = num//100
    cifras_derecha = num%100
    d= cifras_derecha//10
    #cifra_menor =min(u,c,d)
    if u>d and u>=c:
        cifra_menor = u
    else :
        if c<= d :
            cifra_menor = c
        else:
            cifra_menor = d
    return cifra_menor
def pregunta_3(num):
    #retornar la suma de las dos cifras menores
    return None
def pregunta_4(num):
    return None
x = 0
print(pregunta_2(x))