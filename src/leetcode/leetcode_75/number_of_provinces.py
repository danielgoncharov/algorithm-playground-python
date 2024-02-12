from typing import List


class NumberOfProvinces:
    def findCircleNum(
            self,
            isConnected: List[List[int]]
    ) -> int:
        not_visited = set()
        for i in range(len(isConnected)):
            not_visited.add(i)
        visited = set()
        result = 0
        while len(not_visited) != 0:
            node_index = not_visited.pop()
            self.dfs_recursive(isConnected, node_index, visited, not_visited)
            result += 1
        return result

    def dfs_recursive(self, graph, row_index, visited, not_visited):
        if row_index in visited:
            return

        visited.add(row_index)
        if row_index in not_visited:
            not_visited.remove(row_index)

        for column_index in range(len(graph)):
            if graph[row_index][column_index] == 1:
                self.dfs_recursive(graph, column_index, visited, not_visited)
