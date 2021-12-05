hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui

minutos_totales = (min + dura)

while minutos_totales >= 60:
    if minutos_totales >= 60:
        hora +=1
        minutos_totales -= 60
        min = minutos_totales
        if hora >= 24:
            hora -=24
        else: 
            continue
    else:
        print(hora,minutos_totales,sep=":")

print(hora,min,sep=":")
