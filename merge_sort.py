import random


def merge_sort(elements_list):
    if len(elements_list) > 1:
        middle = len(elements_list) // 2
        left = elements_list[:middle]
        right = elements_list[middle:]

        # Llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)

        # Iteradores para recorrer las sublistas
        i = 0
        j = 0

        # Iterador para la lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                elements_list[k] = left[i]
                i += 1
            else:
                elements_list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            elements_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            elements_list[k] = right[j]
            j += 1
            k += 1

    return elements_list


if __name__ == '__main__':
    print('**** ORDENAMIENTO POR MEZCLA')
    list_length = int(input('➡ Define el tamaño de la lista: '))
    numbers_list = [random.randint(0, 100) for i in range(list_length)]

    print(numbers_list)
    print('-' * 20)

    ordered_list = merge_sort(numbers_list)
    print(ordered_list)
