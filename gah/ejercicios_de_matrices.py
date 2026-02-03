
def pregunta_1(mat):
    #retorna el promedio de la fila 1 (índice 0)
    total_elementos = len(mat[0])
    suma = 0
    for j in range(0,total_elementos):
        suma = suma + mat[0][j]
    promedio_fila0 = suma / total_elementos
    return promedio_fila0

def pregunta_2(fila_idx, matriz): #fila_idx es el índice de la fila que quieres
    #retorna el promedio de la fila "fila_idx"
    suma = 0
    for j in range(0,len(matriz[0])):
        suma = suma + matriz[fila_idx][j]
    promedio = suma / len(matriz[0])
    return promedio

def pregunta_3(mat):
    #retornar el promedio de la columna 3 (índice 2)
    total_elementos = len(mat)
    suma = 0
    for i in range(0,len(mat)):
        suma = suma + mat[i][2]

    promedio = suma/total_elementos
    return promedio

def pregunta_4(col_idx, unaMatriz):
    # retornar el promedio de una columna "col_idx"
    suma = 0
    for i in range(0, len(unaMatriz)):
        suma = suma + unaMatriz[i][col_idx]
    promedio = suma / len(unaMatriz)
    return promedio


def pregunta_5(datos):
    #retornar el menor elemento de toda la matriz "datos"
    menor = datos[0][0]
    for i in range(0,len(datos)):
        for j in range(0, len(datos[0])):
            if datos[i][j]< menor:
                menor = datos[i][j]
    return menor

notas = [[18, 17, 20, 16, 17],
         [ 5, 10, 20,  2, 17],
         [12, 14, 15, 19,  9],
         [18, -80, 12, 11, 10]]

#pruebita:
y = pregunta_5(notas)
print("El resultado es:", y)