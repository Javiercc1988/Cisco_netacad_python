def l100kmtompg(liters):
    a_millas = 100*1000/1609.344
    a_galones = liters/3.785411784
    
    total = a_millas / a_galones
    
    return total
    

def mpgtol100km(miles):
    a_km = miles*1609.344/1000
    galon= 3.785411784
    
    total = galon/a_km*100
    
    return total


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))