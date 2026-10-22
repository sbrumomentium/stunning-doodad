
def suma_borde(mat: list[list]) -> int:
    suma = 0
    for fila in mat:
        for num in fila:
            suma = suma + num
    return suma

filas= int(input("Filas: "))
columnas = int (input("Columnas: "))
mat = []
for f in range(filas):
   unaFila = [0] * columnas
   mat.append(unaFila)
for f in range(filas):
   for c in range(columnas):
       print("%4d" % (mat[f][c]),end="")
   print()
#m1 = crear_matriz(filas,columnas)