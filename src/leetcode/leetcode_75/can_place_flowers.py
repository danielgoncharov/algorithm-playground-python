from typing import List


class CanPlaceFlowers:
    def canPlaceFlowers(
            self,
            flowerbed: List[int],
            n: int
    ) -> bool:
        for index in range(len(flowerbed)):
            is_left_zero = flowerbed[index - 1] == 0 if index - 1 >= 0 else True
            is_right_zero = flowerbed[index + 1] == 0 if index + 1 < len(flowerbed) else True
            if is_left_zero and is_right_zero and flowerbed[index] == 0:
                n -= 1
                flowerbed[index] = 1
        return n <= 0
