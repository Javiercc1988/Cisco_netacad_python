palabra1 = input("Introduce una palabra: ").lower()
palabra2 = input("Introduce una palabra: ").lower()

palabra1_ordenada = list(palabra1)
palabra2_ordenada = list(palabra2)

palabra1_ordenada.sort()
palabra2_ordenada.sort()

palabra1_ordenada = "".join(palabra1_ordenada)
palabra2_ordenada = "".join(palabra2_ordenada)

anagrama = (palabra1_ordenada == palabra2_ordenada)

if anagrama:
    print("Son anagramas")
else:
    print("No son anagramas")
