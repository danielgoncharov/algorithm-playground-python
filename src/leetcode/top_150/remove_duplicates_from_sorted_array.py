from typing import List


class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
                result.append(num)
        nums[0:] = result[0:]
        return len(result)
