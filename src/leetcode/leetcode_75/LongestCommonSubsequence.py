class LongestCommonSubsequence:
    def longestCommonSubsequence(
            self,
            text1: str,
            text2: str
    ) -> int:

        memory_array = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    memory_array[i][j] = memory_array[i - 1][j - 1] + 1
                else:
                    memory_array[i][j] = max(
                        memory_array[i - 1][j],
                        memory_array[i][j - 1]
                    )
        return memory_array[len(text2)][len(text1)]
