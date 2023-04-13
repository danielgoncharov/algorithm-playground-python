NOT_SET = -1


def solution(items):
    cache = [[NOT_SET for _ in range(len(items))] for _ in range(3)]
    return count_lucky_numbers(items, 0, 1, 2, cache)


def count_lucky_numbers(
        items,
        index,
        previous_element,
        sequence_counter,
        cache
):
    if index == len(items):
        return 0
    if cache[sequence_counter][index] != NOT_SET:
        return cache[sequence_counter][index]
    if items[index] % previous_element != 0:
        return 0

    if sequence_counter == 0 and items[index] % previous_element == 0:
        return 1
    counter = 0
    for i in range(index + 1, len(items)):
        counter += count_lucky_numbers(items, i, items[index], sequence_counter - 1, cache)
    cache[sequence_counter][index] = counter
    return cache[sequence_counter][index]
