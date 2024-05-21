

print("Bienvenidos al banco del pichincha: ")
nombre= input("Ingrese su nombre de usuario: ")
tarjeta= input("ingrese el numero de tipo de tarjeta (elija entre: 1,2,3 u otro): ")
limite_credito = float(input("Ingrese limite de credito anterior: "))

match (tarjeta):
    case ("1"):
        limite_actual = limite_credito*1.25
        print(f"Estimad@ {nombre} su limite de credito actual es: {limite_actual}")
    case ("2"):
        limite_actual = limite_credito*1.35
        print(f"Estimad@ {nombre} su limite de credito actual es: {limite_actual}")
    case ("3"):
        limite_actual = limite_credito*1.40
        print(f"Estimad@ {nombre} su limite de credito actual es: {limite_actual}")
    case _:
        limite_actual = limite_credito*1.5
        print(f"Estimad@ {nombre} su limite de credito actual es: {limite_actual}")

print("Gracias por su preferencia")
        
