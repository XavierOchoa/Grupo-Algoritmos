numero_de_alumnos = int(input("Ingresa el número de alumnos: "))

if numero_de_alumnos > 100:
    costo_por_alumno = 20
elif 50 <= numero_de_alumnos <= 100:
    costo_por_alumno = 35
elif 20 <= numero_de_alumnos < 50:
    costo_por_alumno = 40
else:
    costo_por_alumno = 70

costo_total = costo_por_alumno * numero_de_alumnos
print(f"El costo total del pasaje para {numero_de_alumnos} alumnos es de: ${costo_total}")
