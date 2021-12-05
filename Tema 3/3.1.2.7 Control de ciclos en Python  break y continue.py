"""Break: Sale del ciclo inmediatamente, e incondicionalmente termina la operación del ciclo; 
el programa comienza a ejecutar la instrucción más cercana después del cuerpo del ciclo.

Continue: Se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; 
el siguiente turno se inicia y la expresión de condición se prueba de inmediato."""

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")