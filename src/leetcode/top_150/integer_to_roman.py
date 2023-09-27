class IntegerToRoman:
    def intToRoman(self, num: int) -> str:
        items = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X",),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        roman_integer = ""
        index = 0
        while num != 0:
            (current_number, chars) = items[index]
            if num - current_number >= 0:
                roman_integer += chars
                num -= current_number
            else:
                index += 1
        return roman_integer
