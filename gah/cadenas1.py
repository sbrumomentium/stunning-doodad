# import time
# acumulador = ""
# nombre = "UTEC"
# for i in range (0,4):
#     letras = nombre[i]
#     # time.sleep(0.3)
#     acumulador = acumulador + letras
#     print(acumulador)
# print("")
# for letra in nombre:
#     # time.sleep(0.3)
#     print(letra)
def pregunta_1(nombre):
    n_nombre = ""

    for i in range (0,4):
        letra = nombre[i]
        if letra == "e":
            n_nombre = n_nombre + letra

    return n_nombre
print(pregunta_1("thie"))
def pregunta_2(nombre):
    n_nombre = ""
    for i in range (0,len(nombre)):
        .3
        
        letra = nombre[i]
        if (letra != "e" and letra != "i" and letra != "u" and letra != "o" and letra != "a"):
            n_nombre = n_nombre + letra
    return n_nombre
print(pregunta_2("ControlAltEntEr"))
def pregunta_3(nombre):
    n_nombre = ""
    ban="AaEeIiOoUu"
    for i in range (0,len(nombre)):
        letra = nombre[i]
        if letra not in ban:
            n_nombre = n_nombre + letra
    return n_nombre
print(pregunta_3("Mike"))
def pregunta_4(nombre):
    num_count= 0

    for letra in nombre:
        if letra in "AaEeIiOoUu":
            num_count += 1
    return num_count
print(pregunta_4("Michael"))
def pregunta_5(nombre):

    return nombre.replace("M","B").replace("e","u")
print(pregunta_5("Michael"))