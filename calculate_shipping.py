def calcular_envio(zona):
    zona = zona.lower()
    if zona == "local":
        return 5.0
    elif zona == "nacional":
        return 15.0
    elif zona == "internacional":
        return 40.0
    return 10.0  # Zona por defecto