'''
Nombre: Jahir Artemio Casas Espínola
Fecha: 11/10/2022
Ejercicio: Jugando con listas

'''
#Se define las listas
materias = ["Redes", "Programación", "Servidores", "Ingles", "Electronica"]
scores = []
#se emplea la funcion for para mostrar la calificacion por materia 
for cal in materias:
    score = input("¿Qué calificacion sacaste en " + cal + "?")
    scores.append(score)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + scores[i])