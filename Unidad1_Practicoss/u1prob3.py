'''
Nombre: Jahir Artemio Casas Espínola
Fecha: 11/10/2022
Ejercicio: El tremendo AT

'''

#Se piden los datos
isr = float(input("Ingrese ISR que se va a declarar: "))

#se utilizan los if y elif para hacer las operaciones 
if(isr < 0):
    print("Lo sentimos, solo se permiten valores mayores a 0")
elif (isr <= 10000):
    A = isr * 0.05
    print("Su intereses de ISR debe de ser: ", A)
elif(isr >= 10000 & isr <= 20000):
    B = isr * 0.15
    print("Su intereses de ISR debe de ser: ", B)
elif(isr >= 20000 & isr <= 35000):
    C = isr * 0.2
    print("Su intereses de ISR debe de ser: ", C)
elif(isr >= 35000 & isr <= 60000):
    D = isr * 0.3
    print("Su intereses de ISR debe de ser: ", D)
elif(isr > 60000):
    E = isr * 0.45
    print("Su ISR más intereses debe de ser: ", E)