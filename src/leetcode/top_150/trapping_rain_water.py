from typing import List


class TrappingRainWater:
    def trap(self, heights: List[int]) -> int:
        left_elevation = heights[0]
        result = 0
        decrement = 0
        for index in range(1, len(heights)):
            right_elevation = index
            if heights[right_elevation] > heights[left_elevation] and right_elevation - left_elevation == 1:
                left_elevation = right_elevation
            elif heights[right_elevation] > heights[left_elevation]:
                result += (right_elevation - left_elevation - 1) * heights[left_elevation] - decrement
                left_elevation = right_elevation
                decrement = 0
            else:
                decrement += heights[right_elevation]

        return result
