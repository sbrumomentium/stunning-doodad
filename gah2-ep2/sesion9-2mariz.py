mat = [
    [18,17,20,16,17],
    [5,10,20,19,17],
    [12,14,15,19,9],
    [18,20,12,11,10]
]
filas =len(mat)
columnas = len(mat[0])
for f in range(filas):
    for c in range(columnas):
        print("%5d" % mat[f][c],end="")
    print()

suma =0
for f in range(4):
   for c in range(5):
       suma = suma + mat[f][c]
print("La suma de todos los elementos de la matriz es: ", suma)

paises = [ "Canada",
"Italy",
"Germany",
"Japan",
"Kazakhstan",
"Russia",
"South Korea",
"United States" ]
medallas = [
           [ 0, 3, 0 ],
           [ 0, 0, 1 ],
           [ 0, 0, 1 ],
           [ 1, 0, 0 ],
           [ 0, 0, 1 ],
           [ 3, 1, 1 ],
           [ 0, 1, 0 ],
           [ 1, 0, 1 ]
       ]
print()
#--- imprime el encabezado usando formato para que salga como tabla
print("%14s %8s %8s %8s %8s" %("Country", "Gold", "Silver","Bronze","Total"))
print()
for f in range(8):
   #-- se imprime el nombre del pais en 14 lugares
   print("%14s" % (paises[f]), end="")
   suma = 0
   for c in range(3):
       #--- se imprimen la cantidad de medallas del pais
       print("%8d" % (medallas[f][c]), end="")
       suma = suma + medallas[f][c]
   print("%8d" % (suma))
