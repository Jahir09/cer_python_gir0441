'''
Descripccion:Utilizar la sentencia if-elif-else.
Autor: Casas Espínola Jahir Artemio
Fecha: 28 de sep del 2022
'''

year = int(input("Introduce un año:"))

if year % 4 !=0: #No es divisible entre 4
   print('Año común')
elif year % 100 !=0: #año Bisiesto
   
   print('Año Bisiesto')
elif year % 400  !=0: 
    print('Año Comun')
else:
   print('De lo contrario, es un año bisisesto')