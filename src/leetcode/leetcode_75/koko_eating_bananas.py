from typing import List


class KokoEatingBananas:

    def minEatingSpeed(self, piles: List[int], max_time: int) -> int:

        return self.binary_search(piles, max_time)

    def binary_search(self, piles, max_time) -> int:
        min_pile = min(piles)
        max_pile = max(piles)
        search_space = list(range(min_pile, max_pile + 1, 1))
        left, right = 0, len(search_space)
        while left < right:
            mid = left + (right - left) // 2
            if self.is_possible(piles, left, right, max_time, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def is_possible(self, piles, left, right, max_time, min_time_candidate) -> bool:
        left_time = min_time_candidate - left + 1
        right_time = 0
        for index in range(min_time_candidate + 1, right, 1):
            right_time += piles[index] // piles[min_time_candidate]
            leftover = piles[index] % piles[min_time_candidate]
            if leftover > 0:
                right_time += 1
        return left_time + right_time <= max_time
