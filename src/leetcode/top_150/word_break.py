from typing import List


class WordBreak:
    def wordBreak(
            self,
            string: str,
            word_dict: List[str]
    ) -> bool:
        cache = [False] * (len(string) + 1)
        cache[0] = True

        for i in range(1, len(string)+1):
            for j in range(i - 1, -1, -1):
                if cache[j]:
                    word = string[j: i]
                    if word in word_dict:
                        cache[i] = True
                        break
        return cache[len(string)]
