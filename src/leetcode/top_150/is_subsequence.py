class IsSubsequence:
    def isSubsequence(self, left: str, right: str) -> bool:
        if len(left) == 0: return True
        return self.check_substring_rec(0, left, 0, right)

    def check_substring_brute(self, left: str, right: str) -> bool:
        string_start = 0
        for index_substring_candidate in range(len(left)):
            character = left[index_substring_candidate]
            found = False
            for string_index in range(string_start, len(right)):
                if character == right[string_index]:
                    found = True
                    string_start = string_index + 1
                    break
            if not found:
                return False
        return True

    def check_substring_rec(
            self,
            left_index,
            left,
            right_index,
            right
    ) -> bool:
        if left_index == len(left):
            return False
        if right_index == len(right):
            return False
        if left[left_index] == right[right_index] and left_index == len(left) - 1:
            return True
        elif left[left_index] == right[right_index]:
            return self.check_substring_rec(left_index + 1, left, right_index + 1, right)
        else:
            return self.check_substring_rec(left_index, left, right_index + 1, right)
