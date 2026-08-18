# ejercicio 2
# sol = int(input("Ingrese un monto: "))
# dolar = 3.350
# print("Tienes el equivalente de ",round((sol / dolar),2)," dolares")
# # ejercicio 3
# nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print("Cumplira 100 años en: ",2126-edad )
# ejercicio 4
minuto = int(input("Ingresa tiempo en minutos: "))
print("En segundos: ",minuto*60)

# ejercicio 5

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