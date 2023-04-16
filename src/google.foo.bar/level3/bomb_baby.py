def solution(mach_needed_str, facula_needed_str):
    mach_needed = int(mach_needed_str)
    facula_needed = int(facula_needed_str)

    counter = 0

    while mach_needed > 0 and facula_needed > 0:
        if mach_needed == 1 and facula_needed == 1:
            return str(counter)
        if mach_needed > facula_needed:
            counter_increment, new_max = calculate_step(mach_needed, facula_needed)
            mach_needed = new_max
        else:
            counter_increment, new_max = calculate_step(facula_needed, mach_needed)
            facula_needed = new_max
        counter += counter_increment

    return "impossible"


def calculate_step(max_number, min_number):
    diff = max_number - min_number
    counter_increment = diff / min_number
    counter_increment = 1 if counter_increment == 0 else counter_increment
    new_max = max_number - counter_increment * min_number
    return counter_increment, new_max
