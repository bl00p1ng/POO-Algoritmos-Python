import random


def lineal_search(elements_list, objective):
    match = False

    for element in elements_list:
        if element == objective:
            match = True
            break

    return match


if __name__ == '__main__':
    print('**** BÚSQUEDA LINEAL ****')
    list_length = int(input('➡ De qué tamaño será la lista: '))
    number_to_search = int(input('➡ Qué número quieres buscar: '))

    numbers_list = [random.randint(0, 100) for i in range(list_length)]

    found = lineal_search(numbers_list, number_to_search)
    print(numbers_list)
    print(f'El elemento {number_to_search} {"esta" if found else "NO esta"} en la lista')
