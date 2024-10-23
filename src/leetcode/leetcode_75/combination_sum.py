from typing import List


class CombinationSum:
    def combinationSum3(
            self,
            items_in_combinations: int,
            goal_sum: int
    ) -> List[List[int]]:
        result = []
        for i in range(1, 9):
            if goal_sum - i > 0:
                self.collect_combination(
                    i + 1,
                    result,
                    [i],
                    goal_sum - i,
                    items_in_combinations - 1
                )
            elif goal_sum - i == 0 and items_in_combinations == 1:
                result.append([i])
        return result

    def collect_combination(
            self,
            index,
            accumulator,
            current_combinations,
            current_sum,
            items_in_combinations
    ):
        for i in range(index, 10):
            if current_sum - i > 0 and items_in_combinations > 1:
                self.collect_combination(
                    i + 1,
                    accumulator,
                    current_combinations + [i],
                    current_sum - i,
                    items_in_combinations - 1
                )
            elif current_sum - i == 0 and items_in_combinations == 1:
                accumulator.append(current_combinations + [i])
