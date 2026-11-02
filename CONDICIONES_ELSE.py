ingreso = float(input("Escribe el ingreso anual: "))
lim_ingreso = 85528
igv_fijado = 0.18
if ingreso <= lim_ingreso:
    igv = ingreso * igv_fijado - 556.02
else:
    igv = 14839.02 + (ingreso - lim_ingreso) * 0.32
if igv < 0:
    igv = 0.0
igv = round(igv, 0)
print("El impuesto es:", igv, "pesos")


anio = int(input("Ingrese el año: "))
if anio < 1582:
    print("No esta dentro del periodo del calendario Gregor.")
elif anio % 4 != 0:
    print(anio, " es ","Año comun")
elif anio % 100 != 0:
    print(anio, " es ","Año biciesto")
elif anio % 400 != 0:
    print(anio, " es ","Año comun")
else:
    print(anio, " es ","Año biciesto")
