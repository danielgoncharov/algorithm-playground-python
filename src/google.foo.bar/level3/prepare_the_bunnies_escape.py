from collections import deque


def solution(maze):
    min_path = bfs(maze)
    rows, cols = get_dim(maze)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                maze[i][j] = 0
                min_path = min(min_path, bfs(maze))
                maze[i][j] = 1
    return min_path


def bfs(maze):
    graph = to_graph(maze)
    visited = set()
    start = (0, 0)
    rows, cols = get_dim(maze)
    end = (rows - 1, cols - 1)
    queue = deque([(start, [])])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return len(path)+1
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None


def get_dim(maze):
    return len(maze), len(maze[0])


def to_graph(maze):
    rows, cols = get_dim(maze)
    graph = {}
    for i in range(rows):
        for j in range(cols):
            neighbors = []
            if i > 0 and not (maze[i][j] == 1 and maze[i - 1][j] == 1):
                neighbors.append((i - 1, j))
            if i < rows - 1 and not (maze[i][j] == 1 and maze[i + 1][j] == 1):
                neighbors.append((i + 1, j))
            if j > 0 and not (maze[i][j] == 1 and maze[i][j - 1] == 1):
                neighbors.append((i, j - 1))
            if j < cols - 1 and not (maze[i][j] == 1 and maze[i][j + 1] == 1):
                neighbors.append((i, j + 1))
            graph[(i, j)] = neighbors
    return graph
