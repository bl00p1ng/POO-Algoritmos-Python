import random


def insertion_sort(elements_list):
    for i in range(1, len(elements_list)):
        current_value = elements_list[i]
        current_position = i

        while current_position > 0 and elements_list[current_position - 1] > current_value:
            elements_list[current_position] = elements_list[current_position - 1]
            current_position -= 1

        elements_list[current_position] = current_value

    return elements_list


if __name__ == '__main__':
    print('**** ORDENAMIENTO POR INSERCIÓN')
    list_length = int(input('➡ Define el tamaño de la lista: '))
    numbers_list = [random.randint(0, 100) for i in range(list_length)]

    print(numbers_list)
    print(insertion_sort(numbers_list))
