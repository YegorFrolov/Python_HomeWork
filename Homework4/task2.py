# Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя



def get_partitions(elements: list) -> list:
    partitions = []

    def recursive_seeker(curr_elements_in_sequence: list, prev_index: int):

        if len(curr_elements_in_sequence) <= len(elements):
            partitions.append(curr_elements_in_sequence)
        else:
            return

        for i in range(prev_index + 1, len(elements)):
            if elements[prev_index] < elements[i] or prev_index == -1:
                temporal_list = curr_elements_in_sequence.copy()
                temporal_list.append(elements[i])

                recursive_seeker(temporal_list, i)

    recursive_seeker([], -1)
    return partitions


def get_max (lists):
    max_length = 0
    max_list = []
    for current_list in get_partitions(lists):
        if len(current_list) > max_length:
            max_list = current_list
            max_length = len(current_list)
    return max_list


print(get_max([1, 5, 2, 3, 4, 6, 1, 7]))
print(get_max([5, 2, 3, 4, 6, 1, 7]))




