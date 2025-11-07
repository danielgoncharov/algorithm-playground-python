from typing import List


class MaximumAverageSubarray1:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_sum = sum(nums[0:k])
        current_max_average = running_sum / k
        for index in range(0, len(nums) - k):
            running_sum = running_sum - nums[index] + nums[index + k]
            current_max_average = max(current_max_average, running_sum / k)
        return current_max_average
