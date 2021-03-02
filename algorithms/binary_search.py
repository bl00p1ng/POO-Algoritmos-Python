import random


def binary_search(elements_list, start, end, objective):
    print(f'buscando {objective} entre {elements_list[start]} y {elements_list[end - 1]}')
    # Significa que el elemento no esta, pues después de dividir sucesivamente la lista nunca se encontró
    if start > end:
        return False

    medium = (start + end) // 2

    if elements_list[medium] == objective:
        return True
    elif elements_list[medium] < objective:
        return binary_search(elements_list, medium + 1, end, objective)
    else:
        return binary_search(elements_list, start, medium - 1, objective)


if __name__ == '__main__':
    print('**** BÚSQUEDA BINARIA ****')
    list_length = int(input('➡ De que tamaño es la lista? '))
    number_to_search = int(input('➡ Que número quieres encontrar? '))

    numbers_list = sorted([random.randint(0, 100) for i in range(list_length)])

    found = binary_search(numbers_list, 0, len(numbers_list), number_to_search)

    print(numbers_list)
    print(f'El elemento {number_to_search} {"esta" if found else "no esta"} en la lista')
