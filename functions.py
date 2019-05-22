# Imprime toda la lista
def showAll(list):
    for value in list:
        print(value)

# Determina si un valor es par
def isPair(value):
    return (value % 2 == 0)

# Imprime los pares
def showPairs(list):
    for value in list:
        if isPair(value):
            print(value)

# Calcula el promedio de los valores de una lista
def calculateAverage(list):

    # Validar que hayan elementos
    if len(list) == 0:
        return 0

    # Sumar los elementos
    sum = 0
    for value in list:
        sum += value
    
    # Retornar la suma dividida por la cantidad
    return sum / len(list)

# Imprime el promedio de la lista
def showAverage(list):
    print( "Promedio: " + str(calculateAverage(list))  )