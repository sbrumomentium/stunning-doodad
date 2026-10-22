
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

def leer_datos(mat:list[list]):
    filas = len(mat)
    columnas = len(mat[0])
    for f in range(filas):
        for c in range(columnas):
            mat[f][c] = int(input(f"matriz[{f}][{c}] = "))

def multiplicar_matriz_escalar(mat:list[list], escalar:int):
    filas = len(mat)
    columnas = len(mat[0])
    for f in range(filas):
        for c in range(columnas):
            mat[f][c] = mat[f][c] * escalar

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))
m1 = crear_matriz(filas, columnas)
leer_datos( m1 )
imprimir_matriz( m1 )

escalar = int(input("Escalar:"))
multiplicar_matriz_escalar(m1, escalar)
imprimir_matriz( m1 )