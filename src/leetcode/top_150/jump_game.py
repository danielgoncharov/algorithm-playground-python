from typing import List
from collections import deque


class JumpGame:
    def jump(self, nums: List[int]) -> int:
        visited = set()
        nodes = deque([(0, nums[0], 0)])
        final_index = len(nums) - 1
        while nodes:
            (index, jumps, level) = nodes.popleft()
            if index == final_index:
                return level
            max_jump = min(index + jumps + 1, len(nums))
            for next_level_index in range(index + 1, max_jump):
                if next_level_index not in visited:
                    visited.add(next_level_index)
                    nodes.append((next_level_index, nums[next_level_index], level + 1))
