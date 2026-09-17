cant=0
while cant<=3:
    cant = int(input("Numero de gorinkianos: "))
for g in range(1,cant+1):
    print("numero: ",g)
    suma = 0
    for p in range(1,6):
        presion = int(input(f"Presion{p}: "))
        suma = suma + presion
    promedio = suma / 5
    if promedio > 130:
        print("Es hipertenso ",promedio)
    else:
        print("No es hipertenso ",promedio)
