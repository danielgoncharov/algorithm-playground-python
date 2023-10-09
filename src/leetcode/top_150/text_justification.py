from typing import List


class TextJustification:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        words_length = len(words)
        line = []
        line_size = 0
        for index in range(words_length):
            word = words[index]
            min_spaces = len(line) - 1
            if line_size + min_spaces + len(word) + 1 < maxWidth:
                line_size += len(word)
                line.append(word)
            else:
                result.append(self.construct_line(line, maxWidth, line_size))
                line.clear()
                line.append(word)
                line_size = len(word)

        if len(line) == 1:
            result.append(line[0] + " " * (maxWidth - len(line[0])))
        elif len(line) > 1:
            last_line = " ".join(line)
            result.append(last_line + " " * (maxWidth - len(last_line)))
        return result

    def construct_line(self, words: List[str], maxWidth: int, line_size: int) -> str:
        string = words[0]
        words_in_line = len(words)
        space_for_spaces = int(maxWidth - line_size)
        if words_in_line == 1:
            return string + " " * (maxWidth - len(string))
        spaces_per_word = space_for_spaces // int(words_in_line - 1)
        addition_per_interval = space_for_spaces % int(words_in_line - 1)
        for index in range(1, words_in_line):
            string += " " * (spaces_per_word + addition_per_interval) + words[index]
            if addition_per_interval > 0:
                addition_per_interval -= 1
        return string
