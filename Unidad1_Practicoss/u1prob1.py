'''
Nombre: Jahir Artemio Casas Espínola
Fecha: 11/10/2022
Ejercicio: Cuenta de ahorro 

'''
##Se recopilan los datos del usuario y se realizan las operaciones 
inv = float(input("Introduce tu inversion: "))
inte = 0.04
bal1 = inv * (1 + inte)
##Se muestran los resultados obtenidos segun el dato del usuario
print("Balance tras el primer año:" + str(round(bal1, 2)))
bal2 = bal1 * (1 + inte)
print("Balance tras el segundo año:" + str(round(bal2, 2)))
bal3 = bal2 * (1 + inte)
print("Balance tras el tercer año:" + str(round(bal3, 2)))