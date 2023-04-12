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


def print_hi(name):
    print(solution(5, 10))
    print(solution(3, 2))
    print(solution(1000000, 100000))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


