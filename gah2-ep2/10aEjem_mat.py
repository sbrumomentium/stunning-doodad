
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

filas = 3
columnas = 5
m1 = crear_matriz(filas, columnas)
imprimir_matriz( m1 )