from typing import List

LEFT_EDGE = 0
RIGHT_EDGE = 1


class NonOverlappingIntervals:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[RIGHT_EDGE])
        result = 1
        previous_interval = sorted_intervals[0]
        for index in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[index]
            if previous_interval[RIGHT_EDGE] <= current_interval[LEFT_EDGE]:
                result += 1
                previous_interval = current_interval
        return len(intervals) - result
