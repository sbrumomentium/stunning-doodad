def pregunta_1(nombre: str) -> str:
    iniciales = ""
    cantidad_letras = 0
    cantidad_vocales = 0
    nueva_palabra = True
    
    for caracter in nombre:
        if caracter == ' ':
            nueva_palabra = True
        else:
            cantidad_letras += 1
            if caracter in "aeiou":
                cantidad_vocales += 1
            
            if nueva_palabra:
                iniciales += caracter.upper()
                nueva_palabra = False
                
    verificador = cantidad_vocales % 5
    return f"{iniciales}-{cantidad_letras}-{verificador}"


def pregunta_2(esencias: list, stock_ml: list, minimo_ml: int, presentacion_ml: int) -> list:
    resultado = []
    for i in range(len(esencias)):
        stock = stock_ml[i]
        if stock < minimo_ml:
            faltante = minimo_ml - stock
            

            pedir = (faltante // presentacion_ml) * presentacion_ml
            if faltante % presentacion_ml != 0:
                pedir += presentacion_ml
                
            resultado.append(f"{esencias[i]}: {pedir} ml")
            
    return resultado


def pregunta_3(control_calidad: list) -> int:
    max_fallos = 0
    indice_peor_lote = -1
    
    for i in range(len(control_calidad)):
        fallos_actuales = 0
        for j in range(len(control_calidad[i])):
            if control_calidad[i][j] == 0:
                fallos_actuales += 1
                
        if fallos_actuales > max_fallos:
            max_fallos = fallos_actuales
            indice_peor_lote = i
            
    return indice_peor_lote