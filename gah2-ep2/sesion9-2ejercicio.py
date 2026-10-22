poblacion = [
    [106, 107, 111, 133, 221, 767, 1766],
    [502, 635, 809, 947, 1402, 3634, 5268],
    [2, 2, 2, 6, 13, 30, 46],
    [163, 203, 276, 408, 547, 729, 628],
    [2, 7, 26, 82, 172, 307, 392],
    [16, 24, 38, 74, 167, 511, 809]
]

continentes = [
    "Africa",
    "Asia",
    "Australia",
    "Europe",
    "North America",
    "South America"
]
filas = len(poblacion)
columnas = len(poblacion[0])
suma20k = 0
for f in range(filas):
   suma20k = suma20k + poblacion[f][5]
print("La cantidad de habitantes que hubo en todo el mundo en el año 2000: ",suma20k)

aus=0
for c in range(columnas):
    aus = aus + poblacion[2][c]
print("En el hipotético caso que los habitantes de Australia tengan vida inmortal, cuántos habitantes tendrían en total?: ",aus)
#
#--- imprime el encabezado usando formato para que salga como tabla
# sumas = []
# print("%14s %8s %8s %8s %8s %8s %8s" %("Year", "1750", "1800","1900","1950","2000","2050"))
# print()
# for f in range(filas):
#    print("%14s" % (continentes[f]), end="")
#     sumas.append(suma)
#    for c in range(columnas):
#        print("%8d" % (poblacion[f][c]), end="")
#    print()

