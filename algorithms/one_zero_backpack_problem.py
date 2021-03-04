def backpack(backpack_size, objects_weights, objects_values, length):
    # Caso base 1. Si ya no quedan elementos o el morral ya no tiene espacio interrumpe la recursividad
    if length == 0 or backpack_size == 0:
        return 0

    # Caso base 2. Si el elemento es mas grande que el espacio restante del morral se salta ese elemento y se pasa
    # al siguiente
    if objects_weights[length - 1] > backpack_size:
        return backpack(backpack_size, objects_weights, objects_values, length - 1)

    # Caso base 3. Si faltan elementos y hay espacio en el morral se evalúa que decisión se va a tomar
    # Si es el valor máximo se agrega al morral si no no se agrega y se analiza el siguiente elemento
    return max(objects_values[length - 1] +
               backpack(backpack_size - objects_weights[length - 1], objects_weights, objects_values, length - 1),
               backpack(backpack_size, objects_weights, objects_values, length - 1))


if __name__ == '__main__':
    values = [60, 100, 120]  # Esto representa los objetos que se quieren llevar en el morral
    weights = [10, 20, 30]  # Esto representa el tamaño de los objetos
    size = 50  # Esto representa el tamaño del morral
    n = len(values)   # El índice que se va a usar en la función recursiva para recorrer los elementos

    # Valor máximo que se puede obtener
    result = backpack(size, weights, values, n)
    print(result)
