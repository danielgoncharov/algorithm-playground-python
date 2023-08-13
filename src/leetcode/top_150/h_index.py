from typing import List


class HIndex:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        citations_ordered = [0] * length
        for index in range(length):
            order_index = min(length, citations[index])
            if order_index > 0:
                citations_ordered[order_index - 1] += 1

        h_index = 0
        for index in range(length - 1, -1, -1):
            h_index += citations_ordered[index]
            if h_index >= index + 1:
                return index + 1
        return 0
