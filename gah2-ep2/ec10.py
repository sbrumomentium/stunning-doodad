

def imprimir_matriz(mat:list):
    filas = len(mat)
    columnas = len(mat[0])
    for f in range(filas):
        for c in range(columnas):
            print("%4d" % mat[f][c], end='')
        print()
def pregunta_1 (m1,m2):
    filas = len(m1)
    columnas = len(m1[0])
    mr = []
    for f in range(filas):
        lista = []
        for c in range(columnas):
            if m1[f][c] == m2[f][c]:
                lista.append(1)
            else:
                lista.append(0)
        mr.append(lista)
    return mr
m1 = [[4,2,3],[2,3,5],[1,5,4]]
m2 = [[4,2,2],[2,5,5],[1,1,4]]
m3 = pregunta_1(m1,m2)
imprimir_matriz(m3)
def pregunta_2 (s1):
    # filas = len(s1)
    # columnas = len(s1[0])
    acc = []
    for i in range(len(s1)):
        if i % 2 == 0:
            acc.append(s1[i])
        else:
            acc.append(s1[i][::-1])
    return acc
s1 = [[4,2,3],[2,3,5],[1,5,4]]
print(pregunta_2(s1))
import random


def pregunta_3(filas: int, col: int) -> list[list[int]]:

    matriz = []

    for i in range(filas):
        fila = []
        for j in range(col):

            if i == 0 or i == filas - 1 or j == 0 or j == col - 1:
                fila.append(random.randint(20, 40))
            else:
                fila.append(0)
        matriz.append(fila)

    return matriz


def pregunta_4(mat: list[list[int]]) -> int:

    max_suma = -1
    idx_max_suma = -1


    for i in range(len(mat)):
        suma_actual = sum(mat[i])

        if suma_actual > max_suma:
            max_suma = suma_actual
            idx_max_suma = i

    return idx_max_suma
