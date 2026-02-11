notas = [[18,17,20,16,17],
         [5,10,20,19,17],
         [12,14,150,19,9],
         [18,20,12,11,10]]
def pregunta_3(mat):
    total_elementos= len(mat)
    suma=0
    for i in range(0,len(mat)):
        suma=suma+mat[i][2]
    promedio=suma/total_elementos
    return promedio
# print(pregunta_3(notas))
def pregunta_4(col_idx, unaMatriz):
    suma= 0
    for i in range(0,len(unaMatriz)):
        suma=suma+unaMatriz[i][col_idx]
    promedio=suma/len(unaMatriz)
    return promedio
def pregunta_5(datos):
    menor = datos[0][0]

    for i in range(0, len(datos)):
        for j in range (0,len(datos[0])):
            if datos[i][j] < menor:
               menor=datos[i][j]
               j += 1
        i+=1
    return menor
print(pregunta_5(notas))