def pregunta_minus_1(num, expon, potencia):
    #hallar la poten
    num = float(input("Numero: "))
    expon = float(input("Exponente: "))
    potencia = float(num ** expon)
    return potencia

def pregunta_1(base, altura, area):
    #hallar el area de un rectangulo
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = float(base * altura)
    return area

def pregunta_2(base, altura, perimetro):
    #hallar el perimetro de un rectangulo
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    perimetro = float((base*2) + (altura*2))
    return perimetro
def pregunta_3(base, altura, perimetro, respuesta):
    #si el perimetro es impar, retorna "perimetro impar
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    perimetro = float((base*2) + (altura*2))
    if perimetro % 2 == 0:
        respuesta = "perimetro par"
    else :
        respuesta ="perimetro impar"
    return respuesta

x= 0
y= 0
z= 0
w= 0
#print(pregunta_1(x,y,z))
#print(pregunta_2(x,y,z))
#print(pregunta_minus_1(x,y,z))
print(pregunta_3(x,y,z,w))