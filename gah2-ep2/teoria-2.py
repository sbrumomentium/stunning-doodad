
print(-4**2)
print( 2 * 7 // 3 ** 2)
print( 2 + 4 ** 2 % 2 ** 3)
#pemdas aplica

# farenheit= float(input("Ingresa Fahrenheit: "))
# celcius = (farenheit - 32) * 5 / 9
# print("En grados Celcius es: ",celcius)
#
# cadena = input("Numero 3 cifras: ")
# suma = int(cadena[0]) + int(cadena[1]) + int(cadena[2])
# print("La suma de las cifras es :", suma)
# #nose
# digitos = int(input("Ingresa un numero de 3 cifras: "))
# c = digitos // 100
# u = digitos % 10
# d = digitos // 10 % 10
# sumDig = c + u + d
# print("La suma de las cifras es :", sumDig)

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



#isThisPeak = True

edad = int(input("Ingresa edad: "))
if edad >= 18:
    print("No esta permitido")
else:
    print("Esta permitido")
    