from typing import List


class FindPivotIndex:
    def pivotIndex(
            self,
            nums: List[int]
    ) -> int:
        total_sum = sum(nums)
        left = 0
        right = total_sum
        for index in range(len(nums)):
            if index - 1 >= 0:
                left += nums[index - 1]
            right -= nums[index]
            if right == left:
                return index
        return -1
