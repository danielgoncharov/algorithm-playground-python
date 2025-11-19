

class DecodeString:

    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_num = 0
        current_str = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                count_stack.append(current_num)
                string_stack.append(current_str)
                current_num = 0
                current_str = ""
            elif ch == ']':
                repeat_count = count_stack.pop()
                prev_str = string_stack.pop()
                current_str = prev_str + current_str * repeat_count
            else:
                # ch is a letter
                current_str += ch

        return current_str