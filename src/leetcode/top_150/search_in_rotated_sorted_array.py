from typing import List


class SearchInRotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right - left != 1:
            left_num = nums[left]
            right_num = nums[right]

            if left_num <= right_num:
                return self.binary_search(nums, left, right, target)

            middle_index = (left + right) // 2
            middle_num = nums[middle_index]

            if middle_num > left_num:
                if left_num <= target <= middle_num:
                    return self.binary_search(nums, left, middle_index, target)
                else:
                    left = middle_index
            elif middle_num <= target <= right_num:  # middle_num < right_num
                return self.binary_search(nums, middle_index, right, target)
            else:
                right = middle_index
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        else:
            return -1

    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        if right < left:
            return -1
        middle_index = (right + left) // 2
        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] > target:
            return self.binary_search(nums, left, middle_index - 1, target)
        else:
            return self.binary_search(nums, middle_index + 1, right, target)
