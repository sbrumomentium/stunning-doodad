# name = input("Ingrese su nombre: ")
# for letra in name:
#     print(letra)
#
# for i in range(len(name)):
#     print(i, name[i])
cadena = "ingenio en accion"
print(cadena[5:1:-1])
contador = 1
while contador <= 10:
    print(contador)
    if contador == 5:
        continue
    print("************")
    print("************")
    contador += 1
