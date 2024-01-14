from typing import List


class CombinationSum:
    def combinationSum(
            self,
            candidates: List[int],
            target: int
    ) -> List[List[int]]:
        candidates.sort()
        combinations = []
        for index in range(0, len(candidates)):
            self.calculate_combinations(
                combinations,
                [candidates[index]],
                target - candidates[index],
                index,
                candidates
            )
        return combinations

    def calculate_combinations(
            self,
            combinations: List[List[int]],
            combination: List[int],
            target: int,
            start_index: int,
            candidates: List[int]
    ):
        if target == 0:
            combinations.append(combination.copy())
            return
        if start_index == len(candidates) or target < 0:
            return

        for index in range(start_index, len(candidates)):
            combination.append(candidates[index])
            self.calculate_combinations(
                combinations,
                combination,
                target - candidates[index],
                index,
                candidates
            )
            combination.pop()
