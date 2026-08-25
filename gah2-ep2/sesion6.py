# def verificar_nota(nota)->str:
#     if nota >= 10.5:
#         return "aprobo"
#     else:
#         return "vas a mcdonals"
#
# num = int(input("Nota: "))
# respuesta = verificar_nota(num)
# print(respuesta)
#
# def verificar_clima(clima)->str:
#     if clima == 1:
#         return "Verano"
#     elif clima == 2:
#         return "Otono"
#     elif clima == 3:
#         return "Invierno"
#     elif clima == 4:
#         return "Primavera"
#     else:
#         return "No corresponde"
# climnum = int(input("Ingrese clima: "))
# respclima = verificar_clima(climnum)
# print(respclima)

def verificar_edad(edad)->int:
    if 0 <= edad <= 17 :
        return 15
    elif 18 <= edad <= 30:
        return 25
    elif 31 <= edad <= 45:
        return 30
    else :
        return 10

# edadnum = int(input("Ingrese edad: "))
# respnum = verificar_edad(edadnum)
# print(respnum)
print(verificar_edad(17))
print(verificar_edad(18))
print(verificar_edad(46))
