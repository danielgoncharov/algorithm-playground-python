class EditDistance:

    def minDistance(self, word1: str, word2: str) -> int:
        return self.find_min_distance(word1, word2, 0, 0, [])

    def find_min_distance(self, word1, word2, i, j, memo):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.find_min_distance(word1, word2, i + 1, j + 1, memo)
            else:
                insert = 1 + self.find_min_distance(word1, word2, i, j + 1, memo)
                delete = 1 + self.find_min_distance(word1, word2, i + 1, j, memo)
                replace = 1 + self.find_min_distance(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]
