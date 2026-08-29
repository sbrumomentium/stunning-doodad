# def verificar_color(edad)->str:
#     if 360 <= edad <= 427 :
#         return "Violeta"
#     elif 428 <= edad <= 476:
#         return "Azul"
#     elif 477 <= edad <= 497:
#         return "Cyan"
#     elif 498 <= edad <= 570:
#         return "Verde"
#     elif 571 <= edad <= 581:
#         return "Amarillo"
#     elif 582 <= edad <= 618:
#         return "Naranja"
#     elif 619 <= edad <= 780:
#         return "Rojo"
#     else :
#         return "No pertenece al espectro visible"
#
# num = int(input("Color: "))
# respuesta = verificar_color(num)
# print(respuesta)

def verificar_moneda(moneda)->str:
    if moneda == 1 or moneda == 2 or moneda == 5:
        return "Es una Moneda"
    elif moneda == 10 :
        return "Es un billete y sale Macchu Picchu"
    elif moneda == 20:
        return "Es un billete y sale Ciudadela de Chan Chan"
    elif moneda == 50:
        return "Es un billete y sale Templo de Chavin de Huantar"
    elif moneda == 100:
        return "Es un billete y sale Sitio arqueologico de Gran Pajateen"
    elif moneda == 200:
        return "Es un billete y sale Ciudad Sagrada de Caral"
    else:
        return "No existe denominacion"
