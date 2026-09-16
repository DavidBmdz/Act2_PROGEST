def calcular_descuento(subtotal, tipo_cliente):
    # Descuento según el monto
    if subtotal >= 1000:
        desc = 0.15
    elif subtotal >= 500:
        desc = 0.10
    else:
        desc = 0.0

    # Descuento adicional por tipo de cliente
    if tipo_cliente.lower() == "vip":
        desc += 0.10
    elif tipo_cliente.lower() == "frecuente":
        desc += 0.05

    return subtotal * desc