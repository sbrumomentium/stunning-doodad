from math import log, trunc,sqrt


def pregunta1(num1,num2,num3):
    """hallar la suma del mayor y el menor de los 3"""
    return max(num1,num2,num3)+min(num1,num2,num3)
# print(pregunta1(5,4,3))
def pregunta2(num1):
    #retornar la cantidad de cifras
    logaritmo_base_10=log(num1)/log(10)
    cifras=trunc(logaritmo_base_10)+1
    return cifras
numero=52222
respuesta=pregunta2(numero)
# print("la cantidad de cifras es :", respuesta)
def ejemplo3(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2
    distancia  = sqrt((x2-x1)**2+(y2-y1)**2)
    return distancia
# print(ejemplo3(5,4,3,4))
def ejemplo4(num):
    #mi metod
    cifra4=num%10
    cifra3=trunc(num%100/10)
    cifra2=trunc(num%100/100)
    cifra1=trunc(num/1000)

    return cifra1+cifra2+cifra3+cifra4

# print(ejemplo4(3215))
def ejemplo4hardmode(num):
    # mi metod
    cifra4 = num % 10
    cifra3 = trunc(num % 100 / 10)
    cifra2 = trunc(num % 1000 / 100)
    cifra1 = trunc(num / 1000)
    if cifra1%2==1 and cifra2%2==1 and cifra3%2==1 and cifra4%2==1:
        return True
    else: return False
# print (ejemplo4hardmode(3715))
def ejemplo4dev(num):
    # mi metod
    cifra4 = num % 10
    cifra3 = trunc(num % 100 / 10)
    cifra2 = trunc(num % 1000 / 100)
    cifra1 = trunc(num / 1000)
    return cifra1,cifra2,cifra3,cifra4
# print(ejemplo4dev(3715))
def pregunta_s(num):
    suma=0
    while num!=0:
        ultimo=num%10
        suma=suma+ultimo
        num=num//10
    return suma
x=1323
resultado=pregunta_s(x)
print("el resultado es: ",resultado)
def pregunta_i(limite):
    # print("El limite vale: ",limite)
    # i = 1
    # while i<=limite:
    #     print(i)
    #     i=i+1
    # return None
    suma=0
    i=1
    while i<=limite:
        suma=suma+i
        i=i+1
    return suma
print(pregunta_i(10))
def ejemplo_no(limite):
    suma = 0
    i = 1
    while i <= limite:
        if i%2==0 and i%10!=0:
            suma=suma+i

        i = i + 1
    return suma
print(ejemplo_no(10))