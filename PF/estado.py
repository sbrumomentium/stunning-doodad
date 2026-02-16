def calcular_estado_inicial():
    """
    Inicializa el diccionario `estado` con los indicadores clave de la empresa,
    incluyendo todos los flags y contadores que luego se referencian en
    calcular_estado_final().
    """
    empleados = 4
    costo_emp = 2000
    # precio_venta = 4.5
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
        # Contadores y flags temporales
        "TurnosProduccionExtra":            0,
        "DemandaExtraTemporal":             0,
        "EmpleadosTemporales":              0,
        "IncentivosActivos":                False,
        "BrandingActivo":                   False,
        "Aumento_ventas_20porciento":       False,

        # Contadores de duracion (Turnos restantes)
        "TurnosMantenimiento":              0,
        "TurnosIncentivos":                 0,
        "TurnosBranding":                   0,
        "TurnosProteccionCompetidores":     0,
        "TurnosProteccionEcommerce":        0,
        "TurnosVentaExcedentes":            0,
        "Turnos_ventas_20porciento":        0,
        "Pedidos_extra_prox_turno":         0,
        "BloqueoCaosDemanda":               0,
        "BloqueoCaosReputacion":            0
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
    # 1. GENERAR DEMANDA (PEDIDOS)
    # ---------------------------------------------------------
    nivel_reputacion = int(estado["Reputacion del mercado"].split()[1])
    demanda_base = nivel_reputacion * 1000

    if estado["BrandingActivo"]:
        demanda_base = int(demanda_base * 1.10)

    demanda_total = demanda_base + estado["DemandaExtraTemporal"]

    if estado["EcommerceActivo"]:
        demanda_total += 5000

    estado["Pedidos por atender"] = demanda_total

    # 2. VENTA AUTOMÁTICA
    # ---------------------------------------------------------
    inventario_disponible = estado["Inventario"]


    factor_ventas = 1.0
    if estado("Aumento_ventas_20porciento", False) or estado("IncentivosActivos", False):
        factor_ventas = 1.2


    ventas_extra_ecommerce = 2000 if estado["EcommerceActivo"] else 0

    posible_venta = estado["Pedidos por atender"]


    posible_venta = int(posible_venta * factor_ventas) + ventas_extra_ecommerce

    ventas_reales = min(posible_venta, inventario_disponible)

    estado["Unidades vendidas"] = ventas_reales
    estado["Inventario"] -= ventas_reales


    ingresos = ventas_reales * 4.5
    estado["Caja disponible"] += ingresos


    if (estado["Pedidos por atender"] - ventas_reales) > 5000:
        actual = int(estado["Reputacion del mercado"].split()[1])
        if actual > 1:
            estado["Reputacion del mercado"] = f"Nivel {actual - 1}"

    # 3. PAGO DE SUELDOS
    # ---------------------------------------------------------
    total_nomina = estado["Total Salarios"]


    if estado["Caja disponible"] >= total_nomina:
        estado["Caja disponible"] -= total_nomina
    else:
        faltante = total_nomina - estado["Caja disponible"]
        estado["Caja disponible"] = 0
        estado["Deuda pendiente"] += faltante * 1.12

    # 4. GESTIÓN DE CUENTAS POR PAGAR (Crédito Proveedores)
    # ---------------------------------------------------------
    # Recorremos la lista de facturas pendientes
    nuevas_cuentas = []
    deuda_a_pagar_hoy = 0

    for factura in estado["CuentasPorPagar"]:
        factura['turnos'] -= 1
        if factura['turnos'] <= 0:
            deuda_a_pagar_hoy += factura['monto']
        else:
            nuevas_cuentas.append(factura)

    estado["CuentasPorPagar"] = nuevas_cuentas

    if deuda_a_pagar_hoy > 0:
        if estado["Caja disponible"] >= deuda_a_pagar_hoy:
            estado["Caja disponible"] -= deuda_a_pagar_hoy
        else:
            faltante = deuda_a_pagar_hoy - estado["Caja disponible"]
            estado["Caja disponible"] = 0
            estado["Deuda pendiente"] += faltante * 1.12

    # 5. PRODUCCIÓN AUTOMÁTICA (Turnos Extra)
    # ---------------------------------------------------------

    if estado["TurnosProduccionExtra"] > 0:

        parts = estado["Maquinas (total/activas/averiadas)"].split("/")
        activas = int(parts[1])
        prod_base = estado["Produccion_por_maquina"] * estado["Mejorar_proceso"]


        extras = max(0, estado["Cantidad de empleados"] - 4)
        prod_total_auto = (prod_base * activas) * (1 + 0.10 * extras)

        estado["Inventario"] += int(prod_total_auto)
        estado["TurnosProduccionExtra"] -= 1

    # 6. ACTUALIZACIÓN DE CONTADORES Y LIMPIEZA
    # ---------------------------------------------------------


    if estado["Pedidos_extra_prox_turno"] > 0:
        estado["DemandaExtraTemporal"] = estado["Pedidos_extra_prox_turno"]
        estado["Pedidos_extra_prox_turno"] = 0  # Ya se aplicó
    else:

        estado["DemandaExtraTemporal"] = 0


    campos_a_reducir = [
        "TurnosMantenimiento", "TurnosIncentivos", "TurnosBranding",
        "TurnosProteccionCompetidores", "TurnosProteccionEcommerce",
        "TurnosVentaExcedentes", "Turnos_ventas_20porciento"
    ]

    for campo in campos_a_reducir:
        if estado(campo, 0) > 0:
            estado[campo] -= 1


    if estado["TurnosIncentivos"] == 0: estado["IncentivosActivos"] = False
    if estado["TurnosBranding"] == 0: estado["BrandingActivo"] = False
    if estado["TurnosMantenimiento"] == 0: estado["MantenimientoHecho"] = False
    if estado["Turnos_ventas_20porciento"] == 0: estado["Aumento_ventas_20porciento"] = False


    estado["EmpleadosTemporales"] = 0

    # 7. CADUCIDAD DE INSUMOS
    # ---------------------------------------------------------

    if estado["Prohibir Produccion"]:
        perdida = int(estado["Insumos disponibles"] * 0.10)
        estado["Insumos disponibles"] -= perdida


    if estado["TurnosVentaExcedentes"] > 0:
        cantidad_vender = int(estado["Insumos disponibles"] * 0.10)
        ingreso = cantidad_vender * 0.30
        estado["Insumos disponibles"] -= cantidad_vender
        estado["Caja disponible"] += ingreso

    estado["InventarioMesAnterior"] = estado["Inventario"]


    # estado["pagos30"] = estado["pagos60"]
    # estado["pagos60"] = 0
    # estado["pagos60"] = estado["pagos90"]
    # estado["pagos90"] = 0
    return estado
