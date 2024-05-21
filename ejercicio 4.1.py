

import time

precioCompra = float(input("ingrese la cantidad del precio de compra: "))
cantidadPrendas = int(input("ingrese la cantidad de prendas: "))

print("procesando los datos")
print("por favor espere .....")
time.sleep(3)

if cantidadPrendas > 21:
    descuento = 0.1 * precioCompra
    precioFinal = precioCompra- descuento
    print(f"la cantidad de prendas fueron {cantidadPrendas}")
    print(f"el precio final a pagar es de {precioFinal}")

elif cantidadPrendas >= 10 and cantidadPrendas <= 20:
    descuento = 0.05 * precioCompra
    precioFinal = precioCompra- descuento
    print(f"la cantidad de prendas fueron {cantidadPrendas}")
    print(f"el precio final a pagar es de {precioFinal}")

else:
    print(f"la cantidad de prendas fueron {cantidadPrendas}")
    print(f"el precio final a pagar es de {precioCompra}")

