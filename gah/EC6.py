def pregunta_1(n: int) -> str:

    result = ""

    current_num = 1


    for i in range(n):

        for j in range(n):

            result += str(current_num) + " "
            current_num += 1

        result += "\n"

    return result


def pregunta_2(numero: int) -> bool:
    str_num = str(numero)
    digits = [int(d) for d in str_num]


    digit_sum = sum(digits)
    digit_count = len(digits)


    if digit_sum < 2:
        is_sum_prime = False
    else:
        is_sum_prime = True
        for i in range(2, int(digit_sum ** 0.5) + 1):
            if digit_sum % i == 0:
                is_sum_prime = False
                break


    if is_sum_prime and (numero % digit_count == 0):
        return True
    else:
        return False


def pregunta_3(nombre: str) -> str:
    words = nombre.split()


    if len(words) < 2:
        return "ERROR"

    initials = []
    for word in words:

        initials.append(word[0].upper())


    return ".".join(initials)


def pregunta_4(lista: list) -> list:
    if not lista:
        return []


    promedio = sum(lista) / len(lista)


    result = []
    for num in lista:
        if num > promedio:
            result.append(num)


    return result
