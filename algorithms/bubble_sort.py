import random


def bubble_sort(elements_list):
    n = len(elements_list)

    # Itera cada elemento de la lista
    for i in range(n):
        # Por cada elemento recorre la lista hasta el final y luego se va  reduciendo porque los elementos del final ya
        # están ordenados
        # recorrer desde 0 hasta la longitud - lo que ya se recorrió - 1 porque se trabaja con un len
        for j in range(0, n - i - 1):
            if elements_list[j] > elements_list[j + 1]:
                elements_list[j], elements_list[j + 1] = elements_list[j + 1], elements_list[j]

    return elements_list


if __name__ == '__main__':
    print('**** ORDENAMIENTO DE BURBUJA ****')
    list_length = int(input('➡ Ingresa el tamaño de la lista: '))

    numbers_list = [random.randint(0, 100) for i in range(list_length)]
    print(numbers_list)

    ordered_list = bubble_sort(numbers_list)
    print(ordered_list)
