def pregunta_1 ( n : int ) -> str :
    acumulador = ""
    for s in range(n-1,-1,-1):
        acumulador = acumulador + s * n * " " + n * "*"+ "\n"

    return acumulador
print(pregunta_1(4))