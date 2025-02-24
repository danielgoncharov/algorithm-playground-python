from collections import deque


class RemovingStarsFromAString:

    def removeStars(self, string: str) -> str:
        star_queue = deque()
        letter_queue = deque()
        for index in range(len(string)):
            if string[index] == '*':
                star_queue.append((string[index], index))
            else:
                letter_queue.append((string[index], index))

        result = ""
        while len(star_queue) != 0:
            (_, star_element_index) = star_queue[len(star_queue) - 1]
            (letter, char_element_index) = letter_queue[len(letter_queue) - 1]
            if char_element_index > star_element_index:
                result += letter
                letter_queue.pop()
            else:
                star_queue.pop()
                letter_queue.pop()
        while len(letter_queue) != 0:
            (letter, _) = letter_queue.pop()
            result += letter
        return "".join(reversed(result))
