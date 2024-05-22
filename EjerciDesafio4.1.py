def calcular_ganancia(tipo, tamaño, kilos, precio_por_kilo):
    
    if tipo == 'A':
        if tamaño == 1:
            precio_final = precio_por_kilo + 0.20
        elif tamaño == 2:
            precio_final = precio_por_kilo + 0.30
    elif tipo == 'B':
        if tamaño == 1:
            precio_final = precio_por_kilo - 0.30
        elif tamaño == 2:
            precio_final = precio_por_kilo - 0.50
    
    ganancia_total = kilos * precio_final
    return ganancia_total

tipo = input("Ingrese el tipo de uva (A/B): ").upper()
tamaño = int(input("Ingrese el tamaño de la uva (1/2): "))
kilos = float(input("Ingrese la cantidad de kilos producidos: "))
precio_por_kilo = float(input("Ingrese el precio inicial por kilo: "))

ganancia = calcular_ganancia(tipo, tamaño, kilos, precio_por_kilo)
print(f"La ganancia obtenida por la venta de uva es: ${ganancia:.2f}")
