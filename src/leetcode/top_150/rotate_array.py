from typing import List


class RotateArray:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        current_element = nums[0]
        next_index = k % size
        while next_index != 0:
            temp = nums[next_index]
            nums[next_index] = current_element
            current_element = temp
            next_index = self.get_index(next_index, size, k)
        nums[0] = current_element

    def get_index(self, index, size, shift):
        if index == 0:
            return index + shift
        elif index == size:
            return shift - 1
        else:
            return (index + shift) % size
