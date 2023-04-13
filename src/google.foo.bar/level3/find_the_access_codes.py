def solution(items):
    return count_lucky_numbers(items, 0, 1, 2)


def count_lucky_numbers(items, index, previous_element, sequence_counter):
    if index == len(items):
        return 0
    if items[index] % previous_element != 0:
        return 0

    if sequence_counter == 0 and items[index] % previous_element == 0:
        return 1
    counter = 0
    for i in range(index + 1, len(items)):
        counter += count_lucky_numbers(items, i, items[index], sequence_counter - 1)
    return counter
