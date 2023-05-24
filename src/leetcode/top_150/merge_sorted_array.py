from typing import List


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_new = nums1[0:m]
        nums1_new_index = 0
        nums2_index = 0
        result_index = 0
        while nums1_new_index < m or nums2_index < n:
            if nums1_new_index == m:
                nums1[result_index:] = nums2[nums2_index:]
                break
            if nums2_index == n:
                nums1[result_index:] = nums1_new[nums1_new_index:]
                break
            if nums1_new[nums1_new_index] < nums2[nums2_index]:
                nums1[result_index] = nums1_new[nums1_new_index]
                nums1_new_index += 1
            else:
                nums1[result_index] = nums2[nums2_index]
                nums2_index += 1
            result_index += 1
