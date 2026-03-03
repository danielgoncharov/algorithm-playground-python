class EditDistance:

    def minDistance(self, word1: str, word2: str) -> int:
        return self.find_min_distance(0, 0, word1, word2)

    def find_min_distance(
            self,
            word1_index: int,
            word2_index: int,
            word1: str,
            word2: str
    ) -> int:
        if word1_index == len(word1) and word2_index == len(word2):
            return 0
        if word1_index == len(word1):
            return len(word2) - word2_index
        if word2_index == len(word2):
            return len(word1) - word1_index

        return min(
            self.find_min_distance(word1_index + 1, word2_index + 1, word1, word2),
            self.find_min_distance(word1_index, word2_index + 1, word1, word2),
            self.find_min_distance(word1_index + 1, word2_index, word1, word2),
        ) + 1
