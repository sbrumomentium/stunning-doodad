def calcular_estado_inicial():
    """
    Inicializa el diccionario `estado` con los indicadores clave de la empresa,
    incluyendo todos los flags y contadores que luego se referencian en
    calcular_estado_final().
    """
    empleados = 4
    costo_emp = 2000

    return {
        # Indicadores financieros y operativos
        "Caja disponible":                  50000,
        "Inventario":                       0,
        "InventarioMesAnterior":            0,
        "Pedidos por atender":              0,
        "Unidades vendidas":                0,
        "Insumos disponibles":              200000,
        "Cantidad de empleados":            empleados,
        "Total Salarios":                   empleados * costo_emp,
        "Deuda pendiente":                  20000,
        "CuentasPorPagar":                  [],
        "Reputacion del mercado":           "Nivel 3",
        "Multas e indemnizaciones":         0,
        "Maquinas (total/activas/averiadas)":"5/5/0",
        "Produccion_por_maquina":           2000,
        "Mejorar_proceso":                  1.0,

        # Banderas de prohibicion y seguro
        "Prohibir Produccion":              False,
        "Prohibir Compras":                 False,
        "Prohibir Importaciones":           False,
        "Fondo emergencia":                 False,
        "MantenimientoHecho":               False,
        "SeguridadReforzada":               False,
        "ClimaLaboralBueno":                False,
        "DescuentoCompra":                  False,
        "CreditoConcedido":                 False,
        "EcommerceActivo":                  False,
        "pagos90":                          0,
        "pagos60":                          0,
        "pagos30":                          0,
        "Prohibir Contrataciones":          False,
        "CrisisEconomicaActiva":            False,
        # Contadores y flags temporales
        "TurnosProduccionExtra":            0,
        "DemandaExtraTemporal":             0,
        "EmpleadosTemporales":              0,
        "IncentivosActivos":                False,
        "BrandingActivo":                   False,
        "Aumento_ventas_20porciento":       False,
        "CalidadPremiumActiva":             False,
        "VentaExcedentesActiva":            False,

        # Contadores de duracion (Turnos restantes)
        "TurnosMantenimiento":              0,
        "TurnosIncentivos":                 0,
        "BrandingTurnosRestantes":          0,
        "TurnosProteccionCompetidores":     0,
        "TurnosProteccionEcommerce":        0,
        "TurnosVentaExcedentes":            0,
        "Turnos_ventas_20porciento":        0,
        "CampaniaTurnosRestantes":          0,
        "Pedidos_extra_prox_turno":         0,
        "BloqueoCaosDemanda":               0,
        "BloqueoCaosReputacion":            0,
        "TurnosCalidadPremium":             0,
        "Produccion_tercer_mes":            0,
        "BloqueoHuelgas":                   0,
        "BloqueoErroresManual":             0,
        "BloqueoFugaTalento":               0,
        "BloqueoAccidentes":                0,
        "BloqueoRobos":                     0,
        "BloqueoVirus":                     0
    }

def calcular_estado_final(estado):
    """
    Aplica las formulas de calculo al final de cada turno (mes) en el siguiente orden:

    1) Venta automatica
       - El precio de venta se debe cargar de la función calcular_estado_inicial()
       - Vender hasta ‘Pedidos por atender’, descontar de ‘Inventario’
       - Sumar ingresos a ‘Caja disponible’
       - Incrementar ‘Unidades vendidas’
       - Descontar Pedidos por atender’
       - Si no se atiende el total de la demanda, la 'Reputacion del mercado' se reduce un nivel

    2) Actualizacion de pedidos por atender
       - Calcular la demanda del proximo mes a partir de:
         • ‘Reputacion del mercado’
         • Flags permanentes (p. ej. ‘BrandingActivo’, ‘EcommerceActivo’)
         • Incrementos temporales (‘DemandaExtraTemporal’)
       - Almacenar en ‘Pedidos por atender’
       - Fórmula para calcular pedidos nuevos es: 1,000 x (nivel de reputación)
       - Recuerde que el Branding activo aumenta la demanda en 10%
       - Recuerde que tener un e-commerce aumenta la demanda en 5,000 unidades al mes
       - Recurde que la campaña promocional aumenta la demanda en 4,000 unidades al mes
       - Recuerde que el cobranding con una marca o influencer popular ocasiona:
        • Una demanda temporal de 300,000 solo por el primer mes (luego desaparece)
        • Una demanda temporal de 150,000 solo por el segundo mes  (luego desaparece)


    3) Pago de la nomina del mes actual
       - Tomar ‘Sueldos por pagar’
       - Si ‘Caja disponible’ ≥ ‘Sueldos por pagar’:
           • Restar de ‘Caja disponible’
         Sino:
           • Calcula cuanto es lo que falta pagar (‘Sueldos por pagar’ – ‘Caja disponible’)
           • Generar deuda con el 12% de interes total.
           • Poner ‘Caja disponible’ = 0

    4) Generacion de la nomina del proximo mes
       - Calcular ‘Sueldos por pagar’ en base a la cantidad de empleados
           • No se toma en cuenta a los empleados temporales porque a ellos ya se les pago al contratarlos.

    5) Anular multas, accidentes, y demas cartas del caos
       - Esto dependera de la carta del caos que haya salido, y de los flags que tengas activos.

    6) Produccion en automatico
       - Si ‘TurnosProduccionExtra’ > 0:
         • Se produce en automatco la misma cantidad del turno anterior (sin gastar insumos).
         • No debes disminuir ‘TurnosProduccionExtra’ porque dicho valor se reduce en el punto 7)

    7) Actualizacion de flags temporales y decremento de contadores
       - Reducir en 1 las variables contadoras. Por ejemplo:
         • ‘TurnosProduccionExtra’
         • ‘DemandaExtraTemporal’
         • ‘EmpleadosTemporales’
         • Duracion de ‘MejoraProceso’, ‘BrandingActivo’, ‘MantenimientoHecho’, etc.
       - Desactivar (poner a False o 0) cualquier flag cuyo contador llegue a cero

    8) Perdida de insumos:
       - Los meses que no se produce nada, el 10% de insumos caduca.
       - Si la produccion de este mes uso menos inventario que el 10% disponible,
         entonces, el excedente caduca (hasta completar el 10% que vence).
       - Puedes apoyarte de las variables "InventarioMesAnterior" e "Inventario"
    """

    # 1) Venta automatica

    precio_venta = 4.5
    demanda_actual = estado["Pedidos por atender"]
    factor_venta = 1.0
    if "Aumento_ventas_20porciento" in estado and estado["Aumento_ventas_20porciento"]:
        factor_venta += 0.20
    if "IncentivosActivos" in estado and estado["IncentivosActivos"]:
        factor_venta += 0.20
    if "CalidadPremiumActiva" in estado and estado["CalidadPremiumActiva"]:
        factor_venta += 0.20
    capacidad_venta_maxima = int(demanda_actual * factor_venta)
    inventario_actual = estado["Inventario"]
    ventas_reales = min(capacidad_venta_maxima, inventario_actual)


    estado["Unidades vendidas"] = ventas_reales
    estado["Inventario"] -= ventas_reales
    estado["Caja disponible"] += (ventas_reales * precio_venta)

    demanda_insatisfecha = capacidad_venta_maxima - ventas_reales

    if demanda_insatisfecha > 5000:

        nivel_str = estado["Reputacion del mercado"].split()[1]
        nivel_int = int(nivel_str)
        if nivel_int > 1:
            nuevo_nivel = nivel_int - 1
            estado["Reputacion del mercado"] = "Nivel " + str(nuevo_nivel)


    # 2) Actualizacion de pedidos por atender

    nivel_str = estado["Reputacion del mercado"].split()[1]
    nivel_reputacion = int(nivel_str)


    nueva_demanda = nivel_reputacion * 1000


    if "BrandingActivo" in estado and estado["BrandingActivo"]:
        nueva_demanda = int(nueva_demanda * 1.10)


    if "CalidadPremiumActiva" in estado and estado["CalidadPremiumActiva"]:
        nueva_demanda = int(nueva_demanda * 1.20)


    if "EcommerceActivo" in estado and estado["EcommerceActivo"]:
        nueva_demanda += 5000


    if "CampaniaTurnosRestantes" in estado and estado["CampaniaTurnosRestantes"] > 0:
        nueva_demanda += 4000


    if "DemandaExtraTemporal" in estado:
        nueva_demanda += estado["DemandaExtraTemporal"]


    if "Pedidos_extra_prox_turno" in estado and estado["Pedidos_extra_prox_turno"] > 0:
        estado["DemandaExtraTemporal"] = estado["Pedidos_extra_prox_turno"]
        estado["Pedidos_extra_prox_turno"] = 0
    else:

        estado["DemandaExtraTemporal"] = 0


    estado["Pedidos por atender"] = nueva_demanda


    # 3)  Pago de la nomina del mes actual

    total_nomina = estado["Total Salarios"]
    if estado["CrisisEconomicaActiva"]:
        total_nomina = int(total_nomina * 1.10)
    if estado["Caja disponible"] >= total_nomina:
        estado["Caja disponible"] -= total_nomina
    else:

        faltante = total_nomina - estado["Caja disponible"]
        estado["Caja disponible"] = 0
        estado["Deuda pendiente"] += (faltante * 1.12)


    # 4) Generacion de la nomina del proximo mes

    nuevas_cuentas = []
    deuda_a_pagar_hoy = 0

    if "CuentasPorPagar" in estado:
        for deuda in estado["CuentasPorPagar"]:
            deuda["turnos"] -= 1
            if deuda["turnos"] <= 0:
                deuda_a_pagar_hoy += deuda["monto"]
            else:
                nuevas_cuentas.append(deuda)

    estado["CuentasPorPagar"] = nuevas_cuentas

    if deuda_a_pagar_hoy > 0:
        if estado["Caja disponible"] >= deuda_a_pagar_hoy:
            estado["Caja disponible"] -= deuda_a_pagar_hoy
        else:
            faltante = deuda_a_pagar_hoy - estado["Caja disponible"]
            estado["Caja disponible"] = 0
            estado["Deuda pendiente"] += (faltante * 1.12)


    # 5) Anular multas, accidentes, y demas cartas del caos

    estado["Multas e indemnizaciones"] = 0

    # 6) Produccion en automatico

    if "TurnosProduccionExtra" in estado and estado["TurnosProduccionExtra"] > 0:

        prod_base = estado["Produccion_por_maquina"]


        empleados = estado["Cantidad de empleados"]
        extras = empleados - 4

        eficiencia_rrhh = 1 + (0.10 * extras)


        mejora_proceso = estado["Mejorar_proceso"]


        maquinas_str = estado["Maquinas (total/activas/averiadas)"]
        partes = maquinas_str.split("/")
        activas_str = partes[1]
        maquinas_activas = int(activas_str)
        # if estado["IncentivosActivos"] :
        #     estado[]

        produccion_total = (prod_base * maquinas_activas) * eficiencia_rrhh * mejora_proceso


        estado["Inventario"] += int(produccion_total)



    # 7)  Actualizacion de flags temporales y decremento de contadores


    lista_contadores = [
            "TurnosProduccionExtra",
            "CampaniaTurnosRestantes",
            "BrandingTurnosRestantes",
            "TurnosMantenimiento",
            "TurnosIncentivos",
            "TurnosClimaLaboral",
            "TurnosSeguridad",
            "TurnosCalidadPremium",
            "TurnosVentaExcedentes",
            "Turnos_ventas_20porciento",
            "BloqueoCaosDemanda",
            "BloqueoCaosReputacion",
            "ProteccionCompetidores",
            "TurnosProteccionEcommerce",
            "BloqueoHuelgas",
            "BloqueoErroresManual",
            "BloqueoFugaTalento",
            "BloqueoAccidentes",
            "BloqueoRobos",
            "BloqueoVirus"
        ]

    for key in lista_contadores:
        if key in estado and estado[key] > 0:
            estado[key] -= 1

    if estado["BrandingTurnosRestantes"] == 0:
        estado["BrandingActivo"] = False
    if estado["TurnosIncentivos"] == 0:
        estado["IncentivosActivos"] = False
    if estado["TurnosMantenimiento"] == 0:
        estado["MantenimientoHecho"] = False
    if estado["TurnosCalidadPremium"] == 0:
        estado["CalidadPremiumActiva"] = False
    if estado["TurnosVentaExcedentes"] == 0:
        estado["VentaExcedentesActiva"] = False
    if estado["Turnos_ventas_20porciento"] == 0:
        estado["Aumento_ventas_20porciento"] = False

    if "BrandingTurnosRestantes" in estado and estado["BrandingTurnosRestantes"] == 0:

        estado["BrandingActivo"] = False


        if "ReputacionOriginal" in estado:
            estado["Reputacion del mercado"] = estado["ReputacionOriginal"]


    if "TurnosIncentivos" in estado and estado["TurnosIncentivos"] == 0:
        estado["IncentivosActivos"] = False

    if "TurnosMantenimiento" in estado and estado["TurnosMantenimiento"] == 0:
        estado["MantenimientoHecho"] = False

    if "TurnosCalidadPremium" in estado and estado["TurnosCalidadPremium"] == 0:
        estado["CalidadPremiumActiva"] = False

    if "TurnosVentaExcedentes" in estado and estado["TurnosVentaExcedentes"] == 0:
        estado["VentaExcedentesActiva"] = False

    if "Turnos_ventas_20porciento" in estado and estado["Turnos_ventas_20porciento"] == 0:
        estado["Aumento_ventas_20porciento"] = False


    estado["EmpleadosTemporales"] = 0

    estado["Prohibir Produccion"] = False
    estado["Prohibir Compras"] = False
    estado["Prohibir Importaciones"] = False
    estado["Prohibir Contrataciones"] = False
    estado["CrisisEconomicaActiva"] = False

    # 8) Perdida de inventario:

    if "Prohibir Produccion" in estado and estado["Prohibir Produccion"]:
        perdida = int(estado["Insumos disponibles"] * 0.10)
        estado["Insumos disponibles"] -= perdida


    estado["InventarioMesAnterior"] = estado["Inventario"]

    return estado
