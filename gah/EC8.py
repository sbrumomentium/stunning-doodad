def pregunta_1(
    nombres: list[str], edades: list[int], eventos: list[str], evento_filtrado: str
) -> list[str]:
    """
    Parametros:
        nombres (list[str]): nombres de los asistentes
        edades (list[int]): edades correspondientes
        eventos (list[str]): evento al que se inscribio cada persona
        evento_filtrado (str): nombre del evento a filtrar
    Retorna:
        list[str]: nombres de los asistentes validos (evento filtrado y edad >= 18)
    """
    lista_nueva = []
    for i in range (0,len(eventos)):
        if eventos[i] == evento_filtrado and edades[i] >= 18:
            lista_nueva.append(nombres[i])
    return lista_nueva


def pregunta_2(dia: int) -> list[list[str]]:
    """
    Parametros:
        dia (int): numero entre 1 y 30
    Retorna:
        list[list[str]]: matriz calendario modificada
    """
    contador = 1
    matriz = []
    for i in range(0,5):
        fila = []
        for j in range(0,6):

            if contador == dia:
                fila.append(str(contador))
            else:
                fila.append('*')
            contador += 1

        matriz.append(fila)

    return matriz


def pregunta_3(asistencia: list[dict]) -> list[str]:
    """
    Parametros:
        asistencia (list[dict]): lista de diccionarios con datos de asistencia
    Retorna:
        list[str]: nombres de estudiantes con al menos 4 asistencias
    """
    lista_nueva = []
    for elem in asistencia:
        if elem["asistencias"]>=4:
            lista_nueva.append(elem["nombre"])
    return lista_nueva


def pregunta_4(jugadores: list[dict]) -> dict:
    """
    Parametros:
        jugadores (list): lista de diccionarios con claves "nombre" y "equipo"
    Retorna:
        dict: diccionario que agrupa los nombres por equipo
    """
    equipos_agrupados = {}
    for jugador in jugadores:
        nombre = jugador["nombre"]
        equipo = jugador["equipo"]

        if equipo not in equipos_agrupados:
            equipos_agrupados[equipo] = []


        equipos_agrupados[equipo].append(nombre)

    return equipos_agrupados
