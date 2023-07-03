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

    print('Partes ordenadas:')
    (aperture_ordenada, max_escene, min_escene, grandeza_total_aperture) = ordenar_apertura(aperture)

    (partes_ordenadas, grandezas_totales) = ordenar_partes(parts)
    print('Apertura: ',aperture_ordenada)
    for parte in partes_ordenadas:
        print('Parte: ', parte)

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

    print('\nAnimales que mas/menos participaron:')
    print(max_animals)
    print(min_animals)

    print('\nEscena de menor/mayor grandeza total:')
    print(min_escene)
    print(max_escene)

    print('\nPromedio de grandeza:')
    for grand in grandezas_totales:
        grandeza_total_espectaculo += grand
    grandeza_total_espectaculo += grandeza_total_aperture
    escenas_totales = ((m-1)*k)*2
    print(grandeza_total_espectaculo/escenas_totales)


print('EJEMPLO 1')
### Parametros de entrada
ANIMALES = {'Ciempies': 1,
            'Libelula': 2,
            'Gato': 3,
            'Perro': 4,
            'Tapir': 5,
            'Nutria': 6}

n = len(ANIMALES)
# Numero de partes
m = 3
# Numero de escenas de cada parte
k = 2

apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro', 'Gato'], ['Ciempies', 'Tapir', 'Gato'],
            ['Gato', 'Ciempies', 'Libelula']]

parte_1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]

parte_2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro', 'Gato']]

partes = [apertura, parte_1, parte_2]

solution(partes, ANIMALES, n, m, k)
print('\n')

print('EJEMPLO 2')
### Parametros de entrada
ANIMALES = {'Capibara': 1,
            'Loro': 2,
            'Caiman': 3,
            'Boa': 4,
            'Cocodrilo': 5,
            'Cebra': 6,
            'Pantera negra': 7,
            'Tigre': 8,
            'Leon': 9}

n = len(ANIMALES)
# Numero de partes
m = 4
# Numero de escenas de cada parte
k = 3

apertura = [
    ["Caiman", "Capibara", "Loro"],
    ["Boa", "Caiman", "Capibara"],
    ["Cocodrilo", "Capibara", "Loro"],
    ["Pantera negra", "Cocodrilo", "Loro"],
    ["Tigre", "Loro", "Capibara"],
    ["Leon", "Caiman", "Loro"],
    ["Leon", "Cocodrilo", "Boa"],
    ["Leon", "Pantera negra", "Cebra"],
    ["Tigre", "Cebra", "Pantera negra"]
]

parte_1 = [
    ["Caiman", "Capibara", "Loro"],
    ["Tigre", "Loro", "Capibara"],
    ["Tigre", "Cebra", "Pantera negra"]
]

parte_2 = [
    ["Pantera negra", "Cocodrilo", "Loro"],
    ["Leon", "Pantera negra", "Cebra"],
    ["Cocodrilo", "Capibara", "Loro"]
]

parte_3 = [
    ["Boa", "Caiman", "Capibara"],
    ["Leon", "Caiman", "Loro"],
    ["Leon", "Cocodrilo", "Boa"]
]

partes = [apertura, parte_1, parte_2, parte_3]

solution(partes, ANIMALES, n, m, k)
print('\n')