def isYearLeap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def daysInMonth(year, month):
    meses_largos = [1,3,5,7,8,10,12]
    if month in meses_largos:
        return 31
    elif month == 2:
        if isYearLeap(year) == True:
            return 29
        else:
            return 28
    else:
        return 30


def dayOfYear(dd, mm, aaaa):
    a = int((14 - mm) / 12)
    y = aaaa - a
    m = int(mm + (12 * a) - 2)
    d = int(dd + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
    return d

def dia(numero_dia):
    return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"][numero_dia]


num_d = int(input("Introduce un dia: "))
num_m = int(input("Introduce el nº del mes: "))
num_y = int(input("Introduce el nº del año: "))
comprueba_dia = dayOfYear(num_d, num_m, num_y)
print("Esa fecha exacta, se corresponde con el día de la semana: ",dia(comprueba_dia))
