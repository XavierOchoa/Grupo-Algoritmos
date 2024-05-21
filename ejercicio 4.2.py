

import webbrowser

print("bienvenido, Andre")
dia= input("ingrese un dia de la semana: ")

match (dia):
    case "lunes":
        print("hoy debes, hacer ejercicio")
    case "martes":
        print("hoy debes, hacer las compras")
    case "miercoles":
        print("hoy debes, ver peliculas")
        print("¿deseas que te recomiende un canal?")
        tipoWeb=input("dime si o no: ")
        if tipoWeb == "si":
            webbrowser.open_new_tab("https://www.disneyplus.com")

    case "jueves":
        print("hoy debes, hacer deberes")
    case "viernes":
        print("hoy debes, jugar futbol")
    case _:
        print("no existe actividad para este dia") 


