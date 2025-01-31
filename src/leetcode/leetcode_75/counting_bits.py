from typing import List


class CountingBits:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        cache = [0, 1] + [None] * (n - 1)
        for index in range(2, n + 1):
            self.count(index, cache)
        return cache

    def count(self, number, cache):
        if cache[number] is None:
            cache[number] = number % 2 + self.count(number // 2, cache)
        return cache[number]
