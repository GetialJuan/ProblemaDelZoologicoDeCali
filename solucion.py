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

escenas = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro', 'Gato'], ['Ciempies',
'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]

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

## Retorna la grandeza total de una escena (de animales)
## y la la grandeza maxima
def grandeza_total_y_max(escena, grandezas):
    animal0 = escena[0]
    grandeza_total = grandezas[animal0]
    grandeza_max = grandezas[animal0]
    for i in range(1,len(escena)):
        animal1 = escena[i]
        grandeza_total += grandezas[animal1]
        if grandezas[animal1] > grandezas[animal0]:
            grandeza_max = grandezas[animal1]
            animal0 = animal1
    return (grandeza_total, grandeza_max)

p = ['Tapir', 'Nutria', 'Perro']
print(grandeza_total_y_max(p, ANIMALES))