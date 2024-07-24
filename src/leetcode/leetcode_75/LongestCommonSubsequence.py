class LongestCommonSubsequence:
    def longestCommonSubsequence(
            self,
            text1: str,
            text2: str
    ) -> int:
        return self.longestSubsequence(
            0,
            0,
            text1,
            text2,
            0
        )

    def longestSubsequence(
            self,
            index_t1: int,
            index_t2: int,
            text1: str,
            text2: str,
            current_len: int
    ) -> int:
        if index_t1 == len(text1) or index_t2 == len(text2):
            return current_len
        if text1[index_t1] == text2[index_t2]:
            return self.longestSubsequence(
                index_t1 + 1,
                index_t2 + 1,
                text1,
                text2,
                current_len + 1
            )
        else:
            return max(
                self.longestSubsequence(
                    index_t1 + 1,
                    index_t2,
                    text1,
                    text2,
                    current_len
                ),
                self.longestSubsequence(
                    index_t1,
                    index_t2 + 1,
                    text1,
                    text2,
                    current_len
                )
            )
