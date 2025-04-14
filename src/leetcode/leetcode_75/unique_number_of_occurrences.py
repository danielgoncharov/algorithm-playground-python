from typing import List


class UniqueNumberOfOccurrences:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for item in arr:
            occurrences[item] = occurrences.get(item, 0) + 1
        return len(occurrences.values()) == len(set(occurrences.values()))
