'''
Nombre del Alumno: Casas Espínola Jahir Artemio
Fecha: 05/10/22
Modulo 4
'''
def liters_100km_to_miles_gallon(liters):
    millas = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784 
    return millas / gallons


def miles_gallon_to_liters_100km(millas):
    liters = 3.785411784 
    kilom = millas * 1609.344 / 1000 
    kilom100 = kilom / 100
    return liters / kilom100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
