num = 0
while num < 1 or num > 9:
    num = int(input("Numero de 1 a 9: "))

# for tabla in range(1, num+1,2):
#     print(tabla)

if num % 2 != 0:
    inicio = 1
else:
    inicio = 2
for tabla in range(inicio, num+1,2):
    print("Tabla :", tabla)
    for m in range(1,11):
        print(tabla,'x',m,'=',tabla*m)