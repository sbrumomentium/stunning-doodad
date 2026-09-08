# for i in range(2,10,2):
#     print(i)
# suma = 0
# for i in range(1,6):
#     print(i)
#     suma += i
# print(suma)
# for i in range(20,101):
#     if i % 3 == 0 or i % 7 == 0:
#         print(i)
# num = int(input("numero: "))
# for i in range(1,num):
#     if num % i == 0:
#         print(i)
# palitos = int(input("palitos: "))
# contacinco = 0
# for i in range(palitos):
#     print("I",end="")
#     contacinco += 1
#     if contacinco == 5:
#         print(" ",end="")
#         contacinco = 0
#
# def pal_tri (filas:int)->str:
#     for f in range(1,filas+1):
#         print("#"*f)
# print(pal_tri(11))
def pal_tri_inv (filas:int)->str:
    # espacios = filas - 1
    # for f in range(1,filas+1):
    #     print(" "*espacios+"#"*f)
    #     espacios = espacios - 1
    cad =  ""
    for f in range(1,filas+1):
        cad = cad + " "*(filas-f)+"#"*f+"\n"
    return cad
print(pal_tri_inv(11))


def es_primo(n: int) -> bool:

    if n <= 1:
        return False


    if n == 2:
        return True

    if n % 2 == 0:
        return False


    for div in range(3, int(n ** 0.5) + 1, 2):
        if n % div == 0:
            return False

    return True



print(es_primo(11))

print(es_primo(16))

print(es_primo(17))