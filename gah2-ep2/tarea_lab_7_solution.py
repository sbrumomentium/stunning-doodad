def pregunta_1(cadena: str) -> (int, int, int):
    mayusculas = 0
    minusculas = 0
    otros = 0
    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
        else:
            otros += 1
    return (mayusculas, minusculas, otros)
    return None


def pregunta_2(oracion: str) -> str:
    if "what do" in oracion or "why did" in oracion:
        if oracion.endswith("?"):
            return "Pregunta correcta"
        else:
            return oracion + "?"
    return "No es pregunta"
    return None


def pregunta_3(n: int) -> str:
    cadena = "A"
    for _ in range(n):
        nueva_cadena = ""
        for char in cadena:
            if char == "A":
                nueva_cadena += "AB"
            elif char == "B":
                nueva_cadena += "A"
        cadena = nueva_cadena
    return cadena
    return None


def pregunta_4(texto: str) -> int:
    digitos_unicos = set()
    for char in texto:
        if char.isdigit():
            digitos_unicos.add(int(char))
    return sum(digitos_unicos)
    return None
