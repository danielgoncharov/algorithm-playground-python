def solution(x, y):
    number, increment = calculate_axis_number(x, 2, 1)
    increment -= 1
    number, _ = calculate_axis_number(y, increment, number)
    return str(number)


def calculate_axis_number(coordinate, increment, number_start):
    index = 1
    number = number_start
    while index < coordinate:
        number += increment
        increment += 1
        index += 1
    return number, increment
