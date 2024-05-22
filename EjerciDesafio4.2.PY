def calcular_sueldo_semana(horas_trabajadas, pago_por_hora):
    if horas_trabajadas > 50:
        return "No está permitido trabajar más de 50 horas"

    sueldo = 0
    
    if horas_trabajadas <= 40:
        sueldo = horas_trabajadas * pago_por_hora
    elif horas_trabajadas <= 45:
        sueldo = 40 * pago_por_hora + (horas_trabajadas - 40) * 2 * pago_por_hora
    else:
        sueldo = 40 * pago_por_hora + 5 * 2 * pago_por_hora + (horas_trabajadas - 45) * 3 * pago_por_hora
    
    return sueldo

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))
sueldo_semanal = calcular_sueldo_semana(horas_trabajadas, pago_por_hora)
print("El sueldo semanal es:", sueldo_semanal)
