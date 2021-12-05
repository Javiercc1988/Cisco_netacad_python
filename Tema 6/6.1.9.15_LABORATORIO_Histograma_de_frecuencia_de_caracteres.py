archivo = input("Introduce el nombre del archivo: ")

diccionario = {}
texto_limpio = ""

with open(archivo + ".txt", "r") as t:
    texto = t.read().lower()

    for i in texto:
        if i.isalpha():
            if i not in diccionario:
                diccionario[i] = 1
            else:
                diccionario[i] += 1


for i in diccionario:
    print(i,"-->",diccionario[i])