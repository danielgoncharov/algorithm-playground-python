from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        cache = [] * len(nums)
        max_result = 0
        for index in range(len(nums)):
            max_candidate = self.find_max_path(
                index,
                nums
            )
            max_result = max(max_candidate, max_result)
        return max_result

    def find_max_path(
            self,
            current_index,
            nums: List[int]
    ):
        max_next = 0
        for index in range(current_index + 2, len(nums)):
            max_candidate = self.find_max_path(
                index,
                nums
            )
            max_next = max(max_candidate, max_next)
        return nums[current_index] + max_next
