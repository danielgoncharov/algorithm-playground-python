class ReverseVowelsOfString:
    def reverseVowels(self, string: str) -> str:
        left = 0
        right = len(string) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = list(string)
        while right - left > 0:
            left_char = result[left]
            right_char = result[right]
            if left_char.lower() in vowels and right_char.lower() in vowels:
                result[left] = right_char
                result[right] = left_char
                left += 1
                right -= 1

            if left_char.lower() not in vowels:
                left += 1

            if right_char.lower() not in vowels:
                right -= 1

        return ''.join(result)
