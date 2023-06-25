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

totalEscenas = apertura + parte_1 + parte_2


### Funciones de ordenamiento para listas de animales
### animal = (nombre, grandeza)

## insertion_sort modificado para una lista de animales
## complejidad = O(n**2)
def insertion_sort_animals(animales, grandezas):
    for i in range(1, len(animales)):
        animal = animales[i]  # Animal actual a comparar e insertar en la porción ordenada
        j = i - 1  # Índice del animal previo en la porción ordenada

        # Desplazar los animales con grandezas mayores que el animal actual hacia la derecha
        while j >= 0 and grandezas[animales[j]] > grandezas[animal]:
            animales[j + 1] = animales[j]
            j -= 1

        animales[j + 1] = animal  # Insertar el animal actual en su posición correcta


## Contar la participacion de Animales
# countAnimals(list,list) -> list
# Complexity O(n)
# @params scenes -> lista que contiene todas las escenas
# @params animales -> diccionario que contiene todos los animales y su grandeza

def counting_animals(scenes, animals):
    # aux que baja al mismo nivel los elemntos de una lista
    # Complexity O(n)
    def downList(list):
        result = []
        for sublist in list:
            result += sublist
        return result

    animalsInScenes = downList(scenes)
    size = len(animalsInScenes)
    # Initialize count array
    count = [0] * 7  # El 7 representa el valor maximo + 1, este valor viene dado el animal con mayor grandeza

    # Store the count of each elements in count array
    for i in range(0, size):
        count[animals[animalsInScenes[i]]] += 1

    max_v = max(count)
    min_v = min(count[1:])
    countMax = [i for i, x in enumerate(count) if x == max_v]  # Busca TODOS los minimos
    countMin = [i for i, x in enumerate(count) if x == min_v]  # Busca TODOS los maximos
    countMin.append(min_v)  # el ultimo valor es cuantas escenas participo
    countMax.append(max_v)  # el ultimo valor es cuantas escenas participo
    return [countMin, countMax]



## Retorna la grandeza total de una escena (de animales)
## y la  grandeza maxima
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


p = ['Tapir', 'Nutria', 'Perro']
print(grandeza_total_y_max(p, ANIMALES))

#Ordena una escena
def counting_sort(scene, animals):
    size = len(scene)
    output = [0] * size
    # Initialize count array
    count = [0] * 7  # El 7 representa el valor maximo + 1, este valor viene dado el animal con mayor grandeza

    # Store the count of each elements in count array
    for i in range(0, size):
        count[animals[scene[i]]] += 1

    # Store the cummulative count
    for i in range(1, 7):
        count[i] += count[i - 1]
    # Sorting
    i = size - 1
    while i >= 0:
        output[count[animals[scene[i]]] - 1] = list(animals.keys())[list(animals.values()).index(animals[scene[i]])]
        count[animals[scene[i]]] -= 1
        i -= 1

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
        return int(str(grandeza_total)+str(grandeza_max))

    return [output, grandeza_total_y_max(scene, animals)]


# Test Sort
print(counting_sort(p, ANIMALES))

print("****************************Ordenando Todas las Escenas*************")

escenas_Ordenadas_Internas = []
for escena in apertura:
    escenas_Ordenadas_Internas.append(counting_sort(escena, ANIMALES))

#print(aux)



#HAY QUE BUSCAR UNA MEJOR MANERA DE HACERLO SIN USAR TANTA MEMORIA PERO POR SI NO SE PUEDE AHI LO DEJO
#Ordena las escenas segun su grandeza
def counting_sort_scenes(array):
    size = len(array)
    output = [0] * size
    max_v=300
    # Initialize count array
    count = [0] * 300  #URGENTE CAMBIAR ESTO

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i][1]] += 1

    # Store the cummulative count
    for i in range(1, max_v):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i][1]] - 1] = array[i][0]
        count[array[i][1]] -= 1
        i -= 1

    #return output
    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


counting_sort_scenes(escenas_Ordenadas_Internas)
print(escenas_Ordenadas_Internas)

## merge-sort
## complejidad = O(n*log(n))
# merge-sort modificado para listas de animales
def merge_sort_animals(animales, grandezas):
    if len(animales) <= 1:
        return animales

    mid = len(animales) // 2
    left_half = animales[:mid]
    right_half = animales[mid:]

    left_half = merge_sort_animals(left_half, grandezas)
    right_half = merge_sort_animals(right_half, grandezas)

    return merge_animals(left_half, right_half, grandezas)


# merge modificado para listas de animales
def merge_animals(left, right, grandezas):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if grandezas[left[i]] < grandezas[right[j]]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged
