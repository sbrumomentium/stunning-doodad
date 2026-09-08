# frase = input("Frase: ")
# for letra in frase:
#     print(letra)
#     letra = "e"
# de 0 a 7
# for numero in range(7):
#     print(numero)

# for i in range(1,6,2):
#     print(i)
# for i in range(6,1,-1):
#     print(i)
#
# for i in range(42,101,3):
#     print(i)
# for i in range(20,101):
#     if i % 4 == 0 or i % 7 == 0:
#         print(i)
filas = int(input("filas: "))
columnas = int(input("columnas: "))
for fil in range(filas):
    for col in range(columnas):
        print("*",end="")
    print()
