#  Haciendo uso de las respuestas
nm_leones = 15
nm_tigres = 10
respuesta = nm_leones >= nm_tigres
print(respuesta)
#   LAB   Variables ‒ Preguntas y Respuestas
n = int(input("Ingrese un número: "))
print(n >= 100)

# Condiciones y ejecución condicional
#Ejecución condicional: la sentencia if
contador = 122
if contador >= 120:
    print("Dormir y soñar")

contador = 150
if contador >= 120:
    print("Preparar la cama")
    print("Tomar un ducha")
    print("Dormir y soñar")
print("Alimentar perros y ovejas")

# Ejecución condicional: la sentencia if-else

clima = 39
if clima < 20:
    print("salir al parque")
else:
    print("Quedarse en casa sombreado")

print("Tomar el almuerzo")

# Sentencias if-else anidadas
calificacion_restaurante = 5
cantidad_boletos = 0
clima = float(input("Ingrese el clima actual en Grados Celsius: "))
print("El clima actual es: ", clima, "°C")
if clima < 20:
    print("salir al parque")
    if calificacion_restaurante >= 9:
        print("Almorzaremos alli")
    else:
        print("Comeremos Sandwich")
else:
    print("Iremos al cine")
    if cantidad_boletos > 0:
        print("Veremos una pelicula")
    else:
        print("Iremos de Shoping al Real Plaza")
print("de vuelta a casa")
