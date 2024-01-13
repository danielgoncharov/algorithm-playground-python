from typing import List


class ContainsDuplicate:
    def containsNearbyDuplicate(
            self,
            nums: List[int],
            k: int
    ) -> bool:
        similar_item_dict = {}
        for index in range(len(nums)):
            value = nums[index]
            indexes = similar_item_dict.get(value)
            if indexes is None:
                similar_item_dict[value] = [index]
            else:
                indexes.append(index)

        for dict_item in similar_item_dict.values():
            if len(dict_item) < 2:
                continue
            for index in range(1, len(dict_item)):
                if abs(dict_item[index - 1] - dict_item[index]) <= k:
                    return True
        return False
