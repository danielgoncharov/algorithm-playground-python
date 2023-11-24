import heapq
from typing import List

class IPO:
    def findMaximizedCapital(
            self,
            max_projects_to_pick: int,
            capital_available: int,
            profits: List[int],
            capitals_demand: List[int]
    ) -> int:
        min_heap = []
        max_heap = []
        for i in range(len(profits)):
            heapq.heappush(min_heap, EntryCapAsc(profits[i], capitals_demand[i]))

        for i in range(max_projects_to_pick):
            while min_heap and min_heap[0].capital_requirement <= capital_available:
                suggested_project = heapq.heappop(min_heap)
                heapq.heappush(max_heap,
                               EntryProfitDesc(suggested_project.profit, suggested_project.capital_requirement))
            if not max_heap:
                return capital_available
            max_profit_entry = heapq.heappop(max_heap)
            capital_available += max_profit_entry.profit

        return capital_available


class EntryCapAsc:
    def __init__(self, profit, capital_req):
        self.profit = profit
        self.capital_requirement = capital_req

    def __lt__(self, other):
        return self.capital_requirement < other.capital_requirement

    def __str__(self):
        return f"profit = {self.profit}, capital requirement= {self.capital_requirement}"


class EntryProfitDesc:
    def __init__(self, profit, capital_req):
        self.profit = profit
        self.capital_requirement = capital_req

    def __lt__(self, other):
        return self.profit > other.profit

    def __str__(self):
        return f"profit = {self.profit}, capital requirement= {self.capital_requirement}"
