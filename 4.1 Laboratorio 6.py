"""
Problema propuesto 4.1
Un profesor tiene un salario inicial de $1500, y recibe un incremento
de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6
años? ¿Qué salario ha recibido en cada uno de los 6 años?
"""
salario_inicial = 1500
incremento = 0.10
años = 6
print("Salario inicial: $", salario_inicial)

for año in range(1, años+1):
    salario_inicial += salario_inicial * incremento
    print("Salario al final del año", año, ": $", round(salario_inicial, 2))

print("Salario al cabo de 6 años: ",  round(salario_inicial, 2))