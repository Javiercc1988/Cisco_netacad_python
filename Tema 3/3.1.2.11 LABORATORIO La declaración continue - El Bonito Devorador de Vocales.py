palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord
userWord = input("Introduce una palabra: ").upper()


for letra in userWord:
    if letra in "AEIOU":
        continue
    else:
        palabraSinVocal = palabraSinVocal + letra

print(palabraSinVocal)
	# Completa el cuerpo del ciclo.

# Imprimir la palabra asignada a palabraSinVocal.
