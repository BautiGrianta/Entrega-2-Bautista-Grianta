nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#Inciso A
def crear_estructura(nombres, notas_1, notas_2):
    """Esta funcion recibe una cadena de nombres y dos listas de notas y retorna un diccionario que 
    contiene como clave el nombre del alumno, y su valor es una tupla con las notas del mismo."""
    nombres_filtrados = nombres.replace(" ", "").replace("'", "").replace("\n", "").split(",")
    alumnos = {nombre:[nota_1, nota_2] for nombre, nota_1, nota_2 in zip(nombres_filtrados, notas_1, notas_2)}
    return alumnos

#Inciso B
def promedio_por_estudiante(alumnos):
    """Esta funcion recibe el diccionario creado previamente y retorna otro diccionario que contiene 
    el promedio de notas de cada estudiante."""
    promedio_estudiante = dict()
    for elem in alumnos:
        promedio_estudiante[elem] = sum(alumnos[elem]) / len(alumnos[elem]) if (len(alumnos[elem])> 0) else 0
    return promedio_estudiante

#Inciso C
def promedio_general(promedio_estudiante):
    """Esta funcion recibe el diccionario con el promedio de cada estudiante y retorna un numero real 
    que es el promedio general del curso."""
    return sum(promedio_estudiante.values()) / len(promedio_estudiante) if (len(promedio_estudiante) > 0) else 0

#Inciso D
def promedio_mayor(promedio_estudiante):
    """Esta funcion recibe el diccionario con el promedio de cada estudiante y retorna el nombre del alumno con el mayor promedio."""
    return max(promedio_estudiante.items(), key=lambda x: x[1])[0]

#Inciso E
def calcular_menor_nota (alumnos):
    """Esta funcion recibe el diccionario creado en el primer inciso y retorna el nombre del alumno con la nota mas baja."""
    return min(alumnos.items(), key = lambda x: min(x[1]))[0]
     

alumnos = crear_estructura(nombres, notas_1, notas_2)
promedio_estudiante = promedio_por_estudiante(alumnos)
promedio_general_curso = promedio_general(promedio_estudiante)
alumno_promedio_mayor = promedio_mayor(promedio_estudiante)
menor_nota = calcular_menor_nota(alumnos)

print(promedio_estudiante)
print(f'El promedio general del curso es: {round(promedio_general_curso,2)}')
print(f'El alumno con el mayor promedio es: {alumno_promedio_mayor}')
print(f'El alumno con la nota más baja es: {menor_nota}')