# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.

userWord = input("Introduce una frase: ").upper()

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    print(letra)