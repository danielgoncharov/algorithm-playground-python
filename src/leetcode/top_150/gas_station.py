from typing import List


class GasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        start = None
        for index in range(len(gas)):
            diff_value = gas[index] - cost[index]
            diff.append(diff_value)
            if start is None and diff_value >= 0:
                start = index

        if start == -1 or sum(diff) < 0:
            return -1

        left = start
        right = left + 1
        right = right if right < len(diff) else 0
        total = diff[start]
        current_increment = right
        while left != right:
            total += diff[current_increment]
            if total >= 0:
                right += 1
                right = right if right < len(diff) else 0
                current_increment = right
            else:
                left -= 1
                left = left if left >= 0 else len(diff) - 1
                current_increment = left
        return left
