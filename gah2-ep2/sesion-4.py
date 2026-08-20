#ej3
# num = int(input("Ingrese un numero: "))
#
# es_par = num % 2 == 0
# es_impar = not es_par
# print( es_par * "Es par" )
# print( es_impar * "Es impar")
#
# #ej4
# s1 = float(input("Ingrese primer lado: "))
# s2 = float(input("Ingrese segundo lado: "))
# s3 = float(input("Ingrese tercer lado: "))
#
# Es_triangulo = s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2
# no_Es_triangulo = not Es_triangulo
# print(Es_triangulo * "Es triangulo valido")
# print(no_Es_triangulo * "No es triangulo valido")

#ej5

consumo = int(input("Ingrese el consumo: "))
propina = consumo * 0.05
igv = consumo * 0.18

print("El monto a pagar es: ", consumo + propina + igv)

#ej6

litro = int(input("Ingrese num botellas de un litro: "))
mlitro = int(input("Ingrese num botellas de mas de un litro: "))
monto = litro *1.25 + mlitro *3.75
print("monto: ", monto)

#ej7
num = float(input("Ingrese un numero de cuatro digitos: "))
# cifra1 = int(num%10)
# cifra2 = int(num % 100 // 10)
# cifra3 = int(num % 1000 // 100)
# cifra4 = int(num % 10000 // 100)
cifra1 = num % 10
num = num // 10
cifra2 = num % 10
num = num // 10
cifra3 = num % 10
num = num // 10
cifra4 = num % 10
num = num // 10
print(cifra1+cifra2+cifra3+cifra4)
#ej8
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))
menor = min(num1,num2,num3)
medio = (num1,num2,num3)
mayor = max(num1,num2,num3)


print()
