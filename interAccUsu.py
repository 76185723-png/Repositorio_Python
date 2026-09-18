# print("Dime lo que sea:")
lo_que_sea = input()
print("Hmm...", lo_que_sea, " ...¿en serio?")
#La función input() con un argumento
lo_que_sea = input("Dime lo que sea: ")
print("Hmm...", lo_que_sea, " ...¿en serio?")

numero = float(input("Ingresa un número: "))
resultado = numero ** 2.0
print(numero, "al cuadrado es", resultado)
# Calcular Hipotenusa
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

# Operadores cadena
text1 = "Samuel"
text2 = "Arnol"
print(text1 + text2)

fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")
