
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

def sumar_matrices(m1:list[list], m2)->list[list]:
    filas = len(m1)
    columnas = len(m1[0])
    m3 = crear_matriz(filas, columnas)
    for f in range(filas):
        for c in range(columnas):
            m3[f][c] = m1[f][c] + m2[f][c]
    return m3

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))
m1 = crear_matriz(filas, columnas)
m2 = crear_matriz(filas, columnas)
llenar_aleatorios( m1 )
llenar_aleatorios( m2 )
imprimir_matriz( m1 )
imprimir_matriz( m2 )

m3 = sumar_matrices(m1, m2)
imprimir_matriz( m3 )







