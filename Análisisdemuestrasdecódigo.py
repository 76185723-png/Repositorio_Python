# Análisis de muestras de código

# Se leen dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if numero1 > numero2:
    tamano_numero = numero1
else:
    tamano_numero = numero2

# Imprime el resultado
print("El número más grande es:", tamano_numero)

# Se leen dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if numero1 > numero2: tamano_numero = numero1
else: tamano_numero = numero2

# Imprime el resultado
print("El número más grande es:", tamano_numero)

# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
tamano_numero = numero1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if numero2 > tamano_numero:
    tamano_numero = numero2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if numero3 > tamano_numero:
    tamano_numero = numero3

# Imprime el resultado.
print("El número más grande es:", tamano_numero)
