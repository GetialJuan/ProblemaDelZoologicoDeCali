#### Solucion al Problema del Zoologico de Cali ####

### Parametros de entrada (Primer ejemplo del enunciado)
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

partes = [parte_1, parte_2]


### Funciones de ordenamiento para listas de animales

## Retorna la grandeza total de una escena (de animales)
## y la  grandeza maxima,
# Complexity O(n)
def grandeza_total_y_max(escena, grandezas):
    animal0 = escena[0]
    grandeza_total = grandezas[animal0]
    grandeza_max = grandezas[animal0]
    for i in range(1, len(escena)):
        animal1 = escena[i]
        grandeza_total += grandezas[animal1]
        if grandezas[animal1] > grandezas[animal0]:
            grandeza_max = grandezas[animal1]
            animal0 = animal1
    return (grandeza_total, grandeza_max)

#Ordena una escena
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




def find_max_value(lst):
    if not lst:
        return None
    
    max_value = lst[0]
    
    for num in lst:
        if num > max_value:
            max_value = num
    
    return max_value

## Ordena las escenas segun su grandeza max
def counting_sort_scenes_grandeza_max(array, grandezas_max):
    size = len(array) # Numero de Escenas
    output = [0] * size
    max_index=find_max_value(grandezas_max) + 1
    # Initialize count array
    count = [0] * max_index  #URGENTE CAMBIAR ESTO

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

# ordena una parte.
# una parte es una lista de escenas
def ordenar_parte(parte):
    print("****************************Ordenando Todas las Escenas*************")
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

    counting_sort_scenes_grandeza_max(escenas_Ordenadas_Internas, grandezas_max)
    counting_sort_scenes(escenas_Ordenadas_Internas, grandezas_totales)
    return [escenas_Ordenadas_Internas, grandeza_total_escena]

def counting_sort_parts(parts, grandezas_totales):
    size = len(parts) # Numero de Partes
    output = [0] * size
    max_index=find_max_value(grandezas_totales) + 1
    # Initialize count array
    count = [0] * max_index  #URGENTE CAMBIAR ESTO

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

def ordenar_partes(partes):
    partes_ordenadas = []
    grandezas_totales = []
    for parte in partes:
        parte_ordenada = ordenar_parte(parte)
        partes_ordenadas.append(parte_ordenada)
        grandezas_totales.append(parte_ordenada[1])

    counting_sort_parts(partes_ordenadas, grandezas_totales)
    print(partes_ordenadas)

ordenar_partes(partes)