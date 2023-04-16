IMPOSSIBLE_RESULT = "impossible"


def solution(mach_needed_str, facula_needed_str):
    mach_needed = int(mach_needed_str)
    facula_needed = int(facula_needed_str)

    if mach_needed <= 0 or facula_needed <= 0:
        return IMPOSSIBLE_RESULT

    counter = 0
    while mach_needed > 0 and facula_needed > 0:
        if mach_needed == 1 and facula_needed == 1:
            return str(counter)
        if mach_needed > facula_needed:
            mach_needed -= facula_needed
        else:
            facula_needed -= mach_needed
        counter += 1
    return IMPOSSIBLE_RESULT
