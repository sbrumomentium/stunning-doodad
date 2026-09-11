def ejem6(num:int)->str:
    con = 1
    suma = 0
    while con < num:
        if num % con == 0:
            suma = suma + con
        con = con + 1
    if suma == num:
         return "Es Perfecto"
    else:
         return "No es Perfecto"

print(ejem6(28))
print(ejem6(45))