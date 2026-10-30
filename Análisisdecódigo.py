[respuestasComparacion.py](https://github.com/user-attachments/files/34194514/respuestasComparacion.py)
# Ejemplo 1:
numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))

# Sentencia if
# Elige el número más grande
if numero1 > numero2:
    tamano_numero = numero1
else:
    tamano_numero = numero2
# Mostrar el resultado
print("El número más grande es:", tamano_numero)

[ejemplo2.py](https://github.com/user-attachments/files/34194518/ejemplo2.py)
# Ejemplo 1:
numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))

# Sentencia if
# Elige el número más grande
if numero1 > numero2:tamano_numero = numero1
else:tamano_numero = numero2
# Mostrar el resultado
print("El número más grande es:", tamano_numero)

[ejemplo3.py](https://github.com/user-attachments/files/34194522/ejemplo3.py)
# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))
#  Asumir temporalmente que numero1 es el mayor
tamano_numero = numero1

if numero2 > tamano_numero:
    tamano_numero = numero2

if numero3 > tamano_numero:
    tamano_numero = numero3

if numero4 > tamano_numero:
    tamano_numero = numero4

print("El número más grande es:", tamano_numero)

[ejercicia1.py](https://github.com/user-attachments/files/34194525/ejercicia1.py)
planta = input("Ingresa nombre de la planta: ")

if planta == "Espatifilo":
    print("¡Espatifilo es la mejor planta de todas!")
    exit()
if planta == "ESPATIFILO":
    print("Si - ¡Espatifilo es la mejor planta de todos!")
    exit()
if planta == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILO!")
    exit()# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))

tamano_numero = max(numero1, numero2, numero3, numero4)
print("El número mayor es:", tamano_numero)
else:
    print("¡Espatifilo!, ¡No" , planta, "!")

    [infoAdicionalMAX.py](https://github.com/user-attachments/files/34194527/infoAdicionalMAX.py)
