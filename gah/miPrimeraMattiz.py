
mat = [[18, 17, 20, 16, 17],
       [ 5, 10, 20, 19, 17],
       [12, 14, 15, 19,  9],
       [18, 20, 12, 11, 10]]

#generar una columna con los valores de la cuarta columna (índie 3)
unaColumna = []
for i in range(0, len(mat)):
    unaColumna.append(mat[i][3])

#ahora cámbiale la primera fila por puros 5, 5, 5, 5, 5
for j in range(0,len(mat[0])):
    mat[0][j] = 5
