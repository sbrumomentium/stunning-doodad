def pregunta_1(numVuelosDeIda: int, numVuelosDeRegreso:
int) -> float:
    # Tu solución inicia aquí
    numVuelosDeIda = 25
    numVuelosDeRegreso = 25
    total_pasajeros = (numVuelosDeIda + numVuelosDeRegreso) * 180
    cantidad = total_pasajeros * 22.5
    return cantidad
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.
print(pregunta_1(22,21))
def pregunta_2(anguloEnRadianes: float) -> float:
    # Tu solución inicia aquí
    anguloEnSexagesimales = (anguloEnRadianes * 180) / 3.1415
    return round(anguloEnSexagesimales,2)
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.    
print(pregunta_2(1.57))

def pregunta_3(magnitud: float) -> str:
    # Tu solución inicia aquí
    tipo = "Sismo"
    if magnitud < 2.0:
        tipo = "Micro"
    elif 2.0 <= magnitud < 3.0:
        tipo = "Muy Menor"
    elif 3.0 <= magnitud < 4.0:
        tipo = "Menor"
    elif 4.0 <= magnitud < 5.0:
        tipo = "Ligero"
    elif 5.0 <= magnitud < 6.0:
        tipo = "Moderado"
    elif 6.0 <= magnitud < 7.0:
        tipo = "Fuerte"
    elif 7.0 <= magnitud < 8.0:
        tipo = "Mayor"
    elif 8.0 <= magnitud < 10.0:
        tipo = "Cataclismo"
    else:  # 10.0 or more [cite: 331]
        tipo = "Meteorico"

    return "El sismo es " + tipo
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.
print(pregunta_3(6.9))
def pregunta_4(peso: float, altura: float) -> str:
    # Tu solución inicia aquí
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Bajo Peso"
    elif 18.5 <= imc < 25:
        categoria = "un peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    elif 30 <= imc < 35:
        categoria = "Obesidad Leve"
    elif 35 <= imc < 40:
        categoria = "Obesidad Media"
    else:
        categoria = "Obesidad Morbida"
    return "Ud tiene " + categoria
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.
print(pregunta_4(48.5, 1.60))