frase = "Eleven animals I slam in a net".replace(" ","").lower()
frase = list(frase)
frase2 = frase[:]
frase2.reverse()
print(frase)
print(frase2)

if frase == frase2:
    print("Es un palindromo")
else:
    print("No es un palindromo")
