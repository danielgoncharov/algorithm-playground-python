from typing import List


class TrappingRainWater:

    def trap(self, heights: List[int]) -> int:
        left_support = [0] * len(heights)
        right_support = [0] * len(heights)

        max_wall = -1
        for index in range(0, len(heights)):
            max_wall = max(max_wall, heights[index])
            left_support[index] = max_wall

        max_wall = -1
        for index in range(len(heights) - 1, -1, -1):
            max_wall = max(max_wall, heights[index])
            right_support[index] = max_wall

        result = 0
        for index in range(0, len(heights)):
            result += min(left_support[index], right_support[index]) - heights[index]
        return result
