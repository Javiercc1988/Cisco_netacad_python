fecha = int(input("Introduce los numeros de la fecha formato: AAAAMMDD: "))

lista = list(str(fecha))    #CREAMOS UNA LISTA Y LA RELLENAMOS CON LOS NUMEROS PASADOS A STRING
suma = 0                    #INICIAMOS LA VARIABLE A 0 DONDE SUMAREMOS LOS ELEMENTOS DE LA LISTA
    
while True:
    if(len(lista)> 1):      # SI LA LISTA TIENE MAS POSICIONES DE 1 SE REPETIRA ESTA OPERACION
        for i in range(len(lista)):     #RECORREMOS LA LISTA
            suma += int(lista[i])       #SUMAMOS CADA ELEMENTO DE LA LISTA CONVIRTIENDOLO A INTEGER

        lista = list(str(suma))         #AHORA RELLENAMOS IGUAL QUE ANTES LA LISTA CONVIRTIENDO EL VALOR DE SUMA EN STRING
        suma = 0
    else:
        break   #UNA VEZ QUE EL VALOR ES DE 1 NUMERO YA CORTAMOS EL BUCLE.
    
print(lista)
