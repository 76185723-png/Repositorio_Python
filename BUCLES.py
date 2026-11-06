# Bucle infinito
while True:
    print("Estoy atrapado dentro de un bucle.")
tamanio_numero = -999999999

numero = int(input("Ingrese un número o escriba -1 para detener: "))
while numero != -1:
    if numero > tamanio_numero:
        tamanio_numero = numero
    numero = int(input("Ingrese un número o escriba -1 para detener: "))

print("El número más grande ingresado es:", tamanio_numero)

odd_numero = 0
even_numero = 0

numero = int(input("Ingrese un número o escriba 0 para detener: "))
while numero != 0:
    # Verificar si el número es par o impar
    if numero % 2 == 1:
        # Incrementa el contador de numeros impares
        odd_numero += 1
    else:
        # Incrementa el contador de numeros pares
        even_numero += 1
    numero = int(input("Ingrese un número o escriba 0 para detener: "))

print("Conteo de números impares:", odd_numero)
print("Conteo de números pares:", even_numero)

contador = 5
while contador != 0:
    print("Dentro del bucle.", contador)
    contador -= 1
print("Fuera del bucle.", contador)

numero_secreto = 7

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numero = int(input(""))
while numero != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Ingrese un numero nuevamente: "))

print("El numero es:", numero_secreto, "¡Bien hecho, muggle! ¡Has adivinado mi número secreto!")
