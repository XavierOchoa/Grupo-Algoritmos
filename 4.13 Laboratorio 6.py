"""
Problema propuesto 4.13
Un vendedor ha realizado N ventas y desea saber cuántas fueron
por 10,000 o menos, cuántas fueron por más de 10,000 pero por
menos de 20,000, y cuánto fue el monto de las ventas de cada una y
el monto global.
"""
ventas_menor_igual_10000 = 0
ventas_entre_10000_y_20000 = 0
monto_global = 0
N = int(input("Ingrese el número total de ventas: "))
i = 0

while i < N:
    monto_venta = float(input(f"Ingrese el monto de la venta {i+1}: "))
    if monto_venta <= 10000:
        ventas_menor_igual_10000 += 1
    elif monto_venta <= 20000:
        ventas_entre_10000_y_20000 += 1
    
    monto_global += monto_venta
    i += 1

print(f"Ventas por $10,000 o menos: {ventas_menor_igual_10000}")
print(f"Ventas por más de $10,000 pero por menos de $20,000: {ventas_entre_10000_y_20000}")
print(f"Monto global de ventas: ${monto_global}")
