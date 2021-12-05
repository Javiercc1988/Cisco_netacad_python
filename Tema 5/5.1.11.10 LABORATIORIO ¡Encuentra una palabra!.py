cadena1 = input("Introduce la cadena a buscar: ")
cadena2 = "vcxzxduybfdsobywuefgas"
lista = list(cadena1)

for i in lista:
    valor = cadena2.find(i)
    if valor == -1:
        print("No esta en la cadena")
        break
    
if valor != -1:
    print("Si está en la cadena")
        
    
