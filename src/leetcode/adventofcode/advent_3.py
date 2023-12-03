def advent3_part1():
    file1 = open('adventofcode/advent_3_input', 'r')
    lines = file1.readlines()

    sum = 0
    for row_index in range(len(lines)):
        line = lines[row_index]
        start_num = None
        end_num = None
        number = ""
        for column_index in range(len(line)):
            if line[column_index].isdigit() and start_num is None:
                number += line[column_index]
                start_num = column_index
                end_num = column_index
            elif line[column_index].isdigit():
                number += line[column_index]
                end_num = column_index
            elif start_num and end_num:
                sum += get_number_to_add(lines, row_index, start_num, end_num, int(number))
                start_num = None
                end_num = None
                number = ""
            else:
                start_num = None
                end_num = None
                number = ""


def get_number_to_add(
        lines,
        row_index,
        column_start,
        column_end,
        number
) -> int:
    # check top line
    for column_index in range(column_start - 1, column_end + 1):
        row_index_to_check = row_index - 1
        if column_index < 0 or row_index_to_check < 0 or column_index == len(lines[row_index_to_check]):
            continue
        if not lines[row_index_to_check][column_index].isdigit() and lines[row_index_to_check][column_index] != '.':
            return number

    # check bottom line
    for column_index in range(column_start - 1, column_end + 1):
        row_index_to_check = row_index + 1
        if column_index < 0 or row_index_to_check == len(lines) - 1 or column_index == len(lines[row_index_to_check]):
            continue
        if not lines[row_index_to_check][column_index].isdigit() and lines[row_index_to_check][column_index] != '.':
            return number

    # check left column
    for row_index in range(row_index - 1, row_index + 1):
        column_index_to_check = column_start - 1
        if row_index < 0 or column_index_to_check < 0 or row_index == len(lines):
            continue
        if not lines[row_index][column_index_to_check].isdigit() and lines[row_index][column_index_to_check] != '.':
            return number

    # check right column
    for row_index in range(row_index - 1, row_index + 1):
        column_index_to_check = column_end + 1
        if row_index < 0 or column_index_to_check < 0 or row_index == len(lines):
            continue
        if not lines[row_index][column_index_to_check].isdigit() and lines[row_index][column_index_to_check] != '.':
            return number
    return 0
