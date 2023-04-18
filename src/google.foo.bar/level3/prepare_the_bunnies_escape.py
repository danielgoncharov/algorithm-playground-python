from collections import deque


def solution(maze):
    source = Node(0, 0, 1, maze)
    queue = deque([source])
    distance_map = {source: 1}

    while queue:
        current_node = queue.popleft()

        if current_node.is_exit_pod():
            return distance_map[current_node]

        for child_node in current_node.neighbors():
            if child_node not in distance_map.keys():
                distance_map[child_node] = distance_map[current_node] + 1
                queue.append(child_node)

    return None


class Node:

    def __init__(self, x, y, pen_limit, maze):
        self.x = x
        self.y = y
        self.pen_limit = pen_limit
        self.maze = maze

    def __hash__(self):
        return self.x ^ self.y

    def rows(self):
        return len(self.maze)

    def columns(self):
        return len(self.maze[0])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_exit_pod(self):
        return self.x == self.columns() - 1 and self.y == self.rows() - 1

    def neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        pen_limit = self.pen_limit
        maze = self.maze
        rows = self.rows()
        columns = self.columns()

        if x > 0:
            wall = maze[y][x - 1] == 1
            if wall:
                if pen_limit > 0:
                    neighbors.append(Node(x - 1, y, pen_limit - 1, maze))
            else:
                neighbors.append(Node(x - 1, y, pen_limit, maze))

        if x < columns - 1:
            wall = maze[y][x + 1] == 1
            if wall:
                if pen_limit > 0:
                    neighbors.append(Node(x + 1, y, pen_limit - 1, maze))
            else:
                neighbors.append(Node(x + 1, y, pen_limit, maze))

        if y > 0:
            wall = maze[y - 1][x] == 1
            if wall:
                if pen_limit > 0:
                    neighbors.append(Node(x, y - 1, pen_limit - 1, maze))
            else:
                neighbors.append(Node(x, y - 1, pen_limit, maze))

        if y < rows - 1:
            wall = maze[y + 1][x]
            if wall:
                if pen_limit > 0:
                    neighbors.append(Node(x, y + 1, pen_limit - 1, maze))
            else:
                neighbors.append(Node(x, y + 1, pen_limit, maze))

        return neighbors
