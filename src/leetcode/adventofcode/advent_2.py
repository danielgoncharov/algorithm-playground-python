def advent2_part1():
    file1 = open('adventofcode/input', 'r')
    games = file1.readlines()

    target_dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0
    for game in games:
        max_hash = {}
        game_name, *draws = game.split(":")
        game_id = int(game_name.split(" ")[-1])
        draws = draws[-1].split(";")
        for draw in draws:
            draw_elements = draw.split(",")
            for element in draw_elements:
                color_number = element.strip().split(" ")
                number = int(color_number[0])
                color = color_number[1]
                current_number = max_hash.get(color)
                if current_number is None:
                    max_hash[color] = number
                elif current_number < number:
                    max_hash[color] = number
        is_game_valid = False
        for key, current_number in max_hash.items():
            target_number = target_dict.get(key)
            if current_number > target_number:
                is_game_valid = False
                break
            else:
                is_game_valid = True
        if is_game_valid:
            sum += game_id
    return sum


def advent2_part2():
    file1 = open('adventofcode/input', 'r')
    games = file1.readlines()

    sum = 0
    for game in games:
        min_hash = {}
        draws = game.split(":")[-1].split(";")
        for draw in draws:
            draw_elements = draw.split(",")
            for element in draw_elements:
                color_number = element.strip().split(" ")
                number = int(color_number[0])
                color = color_number[1]
                current_number = min_hash.get(color)
                if current_number is None:
                    min_hash[color] = number
                elif number > current_number:
                    min_hash[color] = number

        power=1
        for value in min_hash.values():
            power *= value
        sum += power
    return sum
