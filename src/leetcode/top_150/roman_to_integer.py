class RomanToInteger:
    def romanToInt(self, romain_integer_str: str) -> int:
        romain_integer_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        length = len(romain_integer_str)
        result = 0
        previous = None
        for index in range(length):
            current_char = romain_integer_str[index]
            current_number = romain_integer_map[current_char]
            if previous is None:
                result += current_number
            elif previous < current_number:
                result += current_number - 2 * previous
            else:
                result += current_number
            previous = current_number
        return result
