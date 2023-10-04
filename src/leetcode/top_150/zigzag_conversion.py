class ZigzagConversion:
    def convert(self, original_string: str, numRows: int) -> str:
        result_array = []
        start = 0
        offset = numRows
        column = ""
        for index in range(len(original_string)):
            if start == 0 and offset != 0:
                column += original_string[index]
                offset -= 1
                if offset == 0:
                    start = numRows - 2
                    result_array.append(column)
                    column = ""
                    offset = numRows
            elif start != 0:
                column += " " * start + original_string[index] + " " * (numRows - start - 1)
                result_array.append(column)
                column = ""
                start -= 1
        if len(column) != 0:
            result_array.append(column + (numRows - len(column)) * " ")

        result = ""
        for row in range(numRows):
            for index in range(len(result_array)):
                result += result_array[index][row].strip()
        return result
