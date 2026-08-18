from math import pi, tan
# peso = float(input("Ingrese el peso en Kilogramos: "))
# altura = float(input("Ingrese la altura en metros: "))
#
# bmi = (peso*1000 / ((altura) ** 2))/1000
# print("El bmi es:", round(bmi,3))
#
# #ej2
#
# x1=int(input("Ingrese x1: "))
# y1=int(input("Ingrese y1: "))
# x2=int(input("Ingrese x2: "))
# y2=int(input("Ingrese y2: "))
# dist=((x2-x1)**2+(y2-y1)**2)**0.5
#
# print("El distancia es:", dist)

#ej3
# num = float(input("Ingrese un numero de tres digitos: "))
#
# cifra1 = int(num%10)
# cifra2 = int(num % 100 // 10)
# cifra3 = int(num % 1000 // 100)
#
# inv = str(cifra1)+str(cifra2)+str(cifra3)
# mult = int(inv)*2
# print("Numero invertido: ",inv)
# print("Numero multiplicado: ",mult)

#ej4

# colores = int(input("Ingrese numero de colores: "))
# c24 = colores // 24
# colores = colores % 24
# c12 = colores // 24
# col = colores % 12
# c6 = colores // 6
# colores = colores % 6
# print(c24, " Cajas de 24 colores")
# print(c12, " Cajas de 12 colores")
# print(c6, " Cajas de 6 colores")
# print(colores, " Colores sobrantes")

# eje5
segundos = int(input("Ingresa tiempo en segundos: "))
dias = segundos // (60 * 60 * 24)
segundos = segundos % (60 * 60 * 24)
#resta
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
#resta
minutos = segundos // 60
segundos = segundos % 60
print(f"{dias}:{horas}:{minutos}:{segundos}")
#eje6
n = int(input("Ingresa un numero entero: "))
s = float(input("Ingresa el s: "))
area = n*s**2 / (4*tan(pi/n))
print("Area: ", area)