from math import sqrt

def veSiEsTriangulo(l1, l2, l3):
#------------------------------
    if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
        return True
    else:
        return False

def veTipoDeTriangulo(l1, l2, l3):
#------------------------------
    if l1==l2 and l1==l3 and l2==l3:
        return("Equilátero")
    elif l1==l2 or l2==l3 or l3==l1:
        return("Isósceles")
    else:
        return("Escaleno")

def areaDelTriangulo(l1, l2, l3):
#------------------------------
    sp = (l1+l2+l3)/2
    return sqrt(sp*(sp-l1)*(sp-l2)*(sp-l3))
