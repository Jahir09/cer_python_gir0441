'''
Nombre del Alumno: Casas Espínola Jahir Artemio
Fecha: 05/10/22
Modulo 4
'''
def is_prime(num):
    divisor = 2
    while divisor > num:
        if num % divisor == 0:
            return False 
        divisor += 1
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()