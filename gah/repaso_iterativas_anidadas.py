import math


# def print_mult(multiplicando: int):
#     multiplicador = 1
#     while multiplicador <= 12:
#         producto = multiplicador * multiplicando
#         print(multiplicando, " * ", multiplicador, " = ", producto)
#         multiplicador += 1
# mult = 1
# while mult <= 12:
#     print(print_mult(mult))
#     mult += 1


# def pregunta_2(n):
#     cad = ""
#     i=1
#     n = 4
#     while i<=n:
#         j=1
#         while j<=n:
#             cad =cad +str(j)
#             j+=1
#         i+=1
#         cad = cad + "\n"
#     return cad
# print(pregunta_2(6))
def pregunta_3(n):
    cad = ""
    i = 1


    while i <= n:
        j = 1

        while j <= i:
            cad = cad + str(j)
            j += 1
        i += 1
        cad = cad + "\n"
    return cad
print(pregunta_3(6))
def pregunta_4(n):
    cad = ""
    i = 1


    while i <= n:
        j = 1

        while j <= i:
            cad = cad + str("#")
            j += 1
        i += 1
        cad = cad + "\n"
    return cad
print(pregunta_4(6))
def pregunta_5(n):
    acumulador = ""
    i = 1
    while i <= n:
        j = 1

        while j <= n:
            if i == j:
                acumulador = acumulador + "# "
            else:
                acumulador = acumulador + "_ "
            j += 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_5(6))

def pregunta_6(n):
    acumulador = ""
    i = 1
    while i <= n:
        j = n

        while j != 0:
            if i == j:
                acumulador = acumulador + "# "
            else:
                acumulador = acumulador + "_ "
            j -= 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_6(6))


def pregunta_n(n):
    acumulador = ""
    i = 1
    while i <= n:
        j = 1

        while j <= n:
            if i == j or j==1 or j==n:
                acumulador = acumulador + "# "
            else:
                acumulador = acumulador + "_ "
            j += 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_n(6))

def pregunta_m(n):
    acumulador = ""
    i = 1
    while i <= n:
        j = 1

        while j <= n:
            if j<=n/2:
                if j==1 or j==i:
                    # and i<(n / 2)
                    acumulador = acumulador + "# "
                else:
                    acumulador = acumulador + "_ "
                j += 1
            else:
                if j==n or j+i==n+1:
                    # and i<(n / 2)
                    acumulador = acumulador + "# "
                else:
                    acumulador = acumulador + "_ "
                j += 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_m(6))

def pregunta_c(n):
    acumulador = ""
    i = 1
    while i <= n:
        j = 1

        while j <= n:
            if j==1 or i==1 or i==n:
                acumulador = acumulador + "# "
            else:
                acumulador = acumulador + "_ "
            j += 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_c(6))
def pregunta_x(n):
    acumulador = ""
    i = 1
    while i <= n:
        j = 1

        while j <= n:
            if  j==i or j+i==n+1:
                acumulador = acumulador + "# "
            else:
                acumulador = acumulador + "_ "
            j += 1
        i += 1
        acumulador = acumulador + "\n"
    return acumulador
print(pregunta_x(6))