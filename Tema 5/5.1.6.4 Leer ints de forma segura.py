def readint(prompt, min, max):
    repetir = True
    while repetir:
        try:
            entrada = int(input(prompt))
    
            assert entrada >= -10 and entrada <= 10
            repetir = False
            return entrada
            
        except ValueError:
            print("Error entrada incorrecta")
            
    
        except AssertionError:
            print("El valor no esta dentro del rango permitido")

v = readint("Ingresa un numero de -10 a 10: ",-10,10)

print("El numero es:", v)