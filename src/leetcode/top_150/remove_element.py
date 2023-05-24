from typing import List


class RemoveElement:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        result = []
        for index in range(len(nums)):
            if nums[index] != val:
                counter += 1
                result.append(nums[index])
        nums[0:] = result[0:]
        return counter
