# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.

userWord = input("Introduce una frase: ").upper()
palabrasinVocal = ""
for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra in "AEIOU":
        palabrasinVocal += letra
        continue
    print("letra buenas:",letra)
    print("letras rechazadas:",palabrasinVocal)