from typing import List


class WordBreak:
    def wordBreak(
            self,
            string: str,
            word_dict: List[str]
    ) -> bool:
        return self.can_segment(0, 0, string, set(word_dict))

    def can_segment(
            self,
            start_index,
            end_index,
            string,
            words_set: set[str]
    ) -> bool:
        if end_index == len(string):
            return False

        current_segment = string[start_index:end_index + 1]
        if current_segment in words_set and end_index == len(string) - 1:
            return True
        elif current_segment in words_set:
            return (
                    self.can_segment(
                        start_index,
                        end_index + 1,
                        string,
                        words_set
                    )
                    or
                    self.can_segment(
                        end_index + 1,
                        end_index + 1,
                        string,
                        words_set
                    )
            )
        else:
            return self.can_segment(start_index, end_index + 1, string, words_set)
