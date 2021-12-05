bloque = "###"
bloque_der = "  #"
bloque_izq = "#  "
bloque_medio = "# #"

diccionario = {
"0":[[bloque],[bloque_medio],[bloque_medio],[bloque_medio],[bloque]],
"1":[[bloque_der]for i in range(5)],
"2":[[bloque],[bloque_der],[bloque],[bloque_izq],[bloque]],
"3":[[bloque],[bloque_der],[bloque],[bloque_der],[bloque]],
"4":[[bloque_medio],[bloque_medio],[bloque],[bloque_der],[bloque_der]],
"5":[[bloque],[bloque_izq],[bloque],[bloque_der],[bloque]],
"6":[[bloque],[bloque_izq],[bloque],[bloque_medio],[bloque]],
"7":[[bloque],[bloque_der],[bloque_der],[bloque_der],[bloque_der]],
"8":[[bloque],[bloque_medio],[bloque],[bloque_medio],[bloque]],
"9":[[bloque],[bloque_medio],[bloque],[bloque_der],[bloque]]}

entrada = input("Introduce una cifra: ")

for i in range(5):
    for j in (entrada):
        print(diccionario[j][i][0], end=" ")
    print()

