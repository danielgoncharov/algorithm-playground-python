from typing import List


class RotateArray:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp
