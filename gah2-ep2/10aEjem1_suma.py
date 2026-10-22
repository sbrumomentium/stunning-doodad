from random import randint
def crear_matriz(filas, columnas):
    mat = []
    for f in range(filas):
        una_fila = [0] * columnas
        mat.append(una_fila)
    return mat

def imprimir_matriz(mat:list):
    filas = len(mat)
    columnas = len(mat[0])
    for f in range(filas):
        for c in range(columnas):
            print("%4d" % mat[f][c], end='')
        print()

def llenar_aleatorios( m1:list[list]):
    filas = len(m1)
    columnas = len(m1[0])
    for f in range(filas):
        for c in range(columnas):
            m1[f][c] = randint(1,50)

def suma_de_elementos(mat:list[list])->int:
    suma = 0
    for fila in mat:
        for num in fila:
            suma = suma + num
    return suma

def suma_del_borde(mat:list[list])->int:
    filas = len(mat)
    columnas = len(mat[0])
    suma = 0
    for f in range(filas):
        for c in range(columnas):
            if f==0 or c==0 or f==filas-1 or c==columnas-1:
                suma = suma + mat[f][c]
    return suma


filas = int(input("Filas:"))
columnas = int(input("Columnas:"))
m1 = crear_matriz(filas, columnas)
llenar_aleatorios(m1)
imprimir_matriz(m1)

print("Total:", suma_de_elementos(m1))
print("Borde:", suma_del_borde(m1))