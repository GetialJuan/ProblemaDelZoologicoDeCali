import time, random, itertools, string
#--------
#### Solucion al Problema del Zoologico de Cali ####

### Funciones de ordenamiento para listas de animales
def find_max_value(lst):
    if not lst:
        return None
    
    max_value = lst[0]
    
    for num in lst:
        if num > max_value:
            max_value = num
    
    return max_value

def find_min_value(lst):
    if not lst:
        return None
    
    min_value = lst[0]
    
    for num in lst:
        if num < min_value:
            min_value = num
    
    return min_value

## Ordena las escenas
## No retorna ningun valor ya que el array es pasado por referenciax
def counting_sort_scenes_grandeza_max(array, grandezas_max):
    size = len(array) # Numero de Escenas
    output = [0] * size
    max_index=find_max_value(grandezas_max) + 1
    # Initialize count array
    count = [0] * max_index  

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i][2]] += 1

    # Store the cummulative count
    for i in range(1, max_index):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        escena = array[i]
        grandeza_max = escena[2]
        output[count[grandeza_max] - 1] = escena
        count[grandeza_max] -= 1
        i -= 1

    #return output
    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

#HAY QUE BUSCAR UNA MEJOR MANERA DE HACERLO SIN USAR TANTA MEMORIA PERO POR SI NO SE PUEDE AHI LO DEJO
#Ordena las escenas segun su grandeza
def counting_sort_scenes(array, grandezas_totales):
    size = len(array) # Numero de Escenas
    output = [0] * size
    max_index=find_max_value(grandezas_totales) + 1
    # Initialize count array
    count = [0] * max_index  #URGENTE CAMBIAR ESTO

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i][1]] += 1

    # Store the cummulative count
    for i in range(1, max_index):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        escena = array[i]
        grandeza_total = escena[1]
        output[count[grandeza_total] - 1] = escena[0]
        count[grandeza_total] -= 1
        i -= 1

    #return output
    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

def counting_sort_parts(parts, grandezas_totales):
    size = len(parts) # Numero de Partes
    output = [0] * size
    max_index=find_max_value(grandezas_totales) + 1
    # Initialize count array
    count = [0] * max_index 

    # Store the count of each elements in count array
    for i in range(0, size):
        count[grandezas_totales[i]] += 1

    # Store the cummulative count
    for i in range(1, max_index):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        part = parts[i]
        grandeza_total = grandezas_totales[i]
        output[count[grandeza_total] - 1] = part
        count[grandeza_total] -= 1
        i -= 1

    #return output
    # Copy the sorted elements into original array
    for i in range(0, size):
        parts[i] = output[i]

def solution(partes, grandezas, n, m, k):
    grandeza_total_espectaculo = 0
    aperture = partes[0] 
    parts = partes[1:]
    animales = grandezas.keys()
    count_animals = {}
    for animal in animales:
        count_animals[animal] = 0

    ## Retorna la grandeza total de una escena (de animales)
    ## y la  grandeza maxima, ademas de ir contando las apariciones
    ## de cada animal
    # Complexity O(n)
    def grandeza_total_y_max(escena, grandezas):
        animal0 = escena[0]
        count_animals[animal0] += 1
        grandeza_total = grandezas[animal0]
        grandeza_max = grandezas[animal0]
        for i in range(1, len(escena)):
            animal1 = escena[i]
            count_animals[animal1] += 1
            grandeza_total += grandezas[animal1]
            if grandezas[animal1] > grandezas[animal0]:
                grandeza_max = grandezas[animal1]
                animal0 = animal1
        return (grandeza_total, grandeza_max)
    
    ## Retorna una escena ordenada de animales junto con la grandeza_total y
    ## la grandeza máxima
    ## output: Escena ordnada
    ## grandeza_total: Suma de las grandezas de la escena
    ## grandeza_max: Grandeza máxima que tiene un animal en la escena
    # Complexity O(n)
    def counting_sort(scene, animals):
        size = len(scene)
        output = [0] * size
        (grandeza_total, grandeza_max) = grandeza_total_y_max(scene, animals)
        # Initialize count array
        max_index = grandeza_max+1
        count = [0] * max_index

        # Store the count of each elements in count array
        for i in range(0, size):
            count[animals[scene[i]]] += 1

        # Store the cummulative count
        for i in range(1, max_index):
            count[i] += count[i - 1]
        # Sorting
        i = size - 1

        animals_list = list(animals.keys())
        grandezas_list = list(animals.values())

        while i >= 0:
            grandeza = animals[scene[i]]
            index = grandezas_list.index(grandeza)
            output[count[grandeza] - 1] = animals_list[index]
            count[grandeza] -= 1
            i -= 1

        return [output, grandeza_total, grandeza_max]
    
    ## Retorna una parte ordenada de escenas junto con su grandeza total de la escena
    ## escenas_Ordenadas_Internas: Parte ordenada de escenas
    ## grandeza_total_escena: Grandeza total de una Parte (Suma de las grandezas de las escenas)
    # una parte es una lista de escenas
    def ordenar_parte(parte):
        escenas_Ordenadas_Internas = []
        grandezas_totales = []
        grandezas_max = []
        grandeza_total_escena = 0
        for escena in parte:
            (escena_ordenada, grandeza_total, grandeza_max) = counting_sort(escena, ANIMALES)
            escenas_Ordenadas_Internas.append((escena_ordenada, grandeza_total, grandeza_max))
            grandezas_totales.append(grandeza_total)
            grandezas_max.append(grandeza_max)
            grandeza_total_escena += grandeza_total
        
        #Ordena las esceneas a partir de su grandeza máxima
        counting_sort_scenes_grandeza_max(escenas_Ordenadas_Internas, grandezas_max)
        counting_sort_scenes(escenas_Ordenadas_Internas, grandezas_totales)
        return [escenas_Ordenadas_Internas, grandeza_total_escena]
    
    def ordenar_partes(partes):
        partes_ordenadas = []
        grandezas_totales = []
        for parte in partes:
            parte_ordenada = ordenar_parte(parte)
            partes_ordenadas.append(parte_ordenada)
            grandezas_totales.append(parte_ordenada[1])

        counting_sort_parts(partes_ordenadas, grandezas_totales)
        return (partes_ordenadas, grandezas_totales)

    def ordenar_apertura(apertura):
        escenas_Ordenadas_Internas = []
        grandezas_totales = []
        grandezas_max = []
        grandeza_total_escena = 0
        for escena in apertura:
            (escena_ordenada, grandeza_total, grandeza_max) = counting_sort(escena, ANIMALES)
            escenas_Ordenadas_Internas.append((escena_ordenada, grandeza_total, grandeza_max))
            grandezas_totales.append(grandeza_total)
            grandezas_max.append(grandeza_max)
            grandeza_total_escena += grandeza_total
        
        escena_max = find_max_value(grandezas_totales)
        escena_min = find_min_value(grandezas_totales)

        counting_sort_scenes_grandeza_max(escenas_Ordenadas_Internas, grandezas_max)
        counting_sort_scenes(escenas_Ordenadas_Internas, grandezas_totales)

        return [escenas_Ordenadas_Internas,
                escenas_Ordenadas_Internas[grandezas_totales.index(escena_max)], 
                escenas_Ordenadas_Internas[grandezas_totales.index(escena_min)],
                grandeza_total_escena]

    (aperture_ordenada, max_escene, min_escene, grandeza_total_aperture) = ordenar_apertura(aperture)

    (partes_ordenadas, grandezas_totales) = ordenar_partes(parts)

    count_animals_values = list(count_animals.values())
    max_animal = find_max_value(count_animals_values)
    min_animal = find_min_value(count_animals_values)

    max_animals = []
    min_animals = []
    for animal in count_animals:
        value = count_animals[animal]
        if value == max_animal:
            max_animals.append([animal, value])
        if value == min_animal:
            min_animals.append([animal, value])

    for grand in grandezas_totales:
        grandeza_total_espectaculo += grand
    grandeza_total_espectaculo += grandeza_total_aperture
    escenas_totales = ((m-1)*k)*2
#-------

## Función que se encarga de generar una variable ANIMALES
## La estructura de la variable ANIMALES correspondera a unas llaves y valores
## que empiezan desde 1 hasta n.
def generador_animales(n):
    animales = {}
    for i in range(1, n+1):
        animales[str(i)] = i
    return animales

## Función que se encarga de generar una apertura aleatoria
## La apertura consta de (m-1)*k escenas
## Retorna un array de una apertura
def generador_apertura(animales, m, k):
    num_escenas = (m-1) * k
    nombres_animales = list(animales.keys())
    apertura = []
    
    for i in range(num_escenas):
        escena = random.sample(nombres_animales, 3)  # Selecciona 3 nombres sin repetición
        apertura.append(escena)
    
    return apertura

## Función que se encarga de generar una parte aleatoria
## La cantidad de partes consta de m-1 partes
## La cantidad de escenas consta de k escenas
## Retorna un array de partes
def generador_partes(animales, m, k):
    num_partes = m-1
    num_escenas = k
    #Convierte en una lsita todos los nombres del diccionario de 'animales'
    nombres_animales = list(animales.keys())
    partes = []
    for x in range (0, num_partes):
        parte = []
        for i in range(num_escenas):
            escena = random.sample(nombres_animales, 3)  # Selecciona 3 nombres sin repetición
            parte.append(escena)
        partes.append(parte)
    return partes


print('PRUEBA')
### Parametros de entrada
ANIMALES = generador_animales(100000000000000000000)

n = len(ANIMALES)
# Numero de partes
m = 1000
# Numero de escenas de cada parte
k = 2

apertura = generador_apertura(ANIMALES, m, k)
partes = generador_partes(ANIMALES, m, k)
partes.insert(0, apertura) #Se inserta a partes la apertura en la primera posición

solution(partes, ANIMALES, n, m, k)

