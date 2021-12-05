def misplit(strng):
    frase = []              #CREAMOS UNA LISTA VACIA
    palabra=""              #CREAMOS UNA VARIABLE DE TEXTO VACIA
    for i in strng:         #RECORREMOS LA FRASE
        if i !=" ":         #SI LA i ES DIFERENTE A UN ESPACIO " " LA AÑADIMOS A LA PALABRA
            palabra += i
        else:   
            if palabra != "":   #SI LA VARIABLE PALABRA ES DIFERENTE A "" (VACIO)
                frase.append(palabra)       #AÑADIMOS A LA LISTA LA PALABRA QUE SE HA FORMADO
                palabra = ""                
                
    if palabra != "":   
        frase.append(palabra)
    
    return frase

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
