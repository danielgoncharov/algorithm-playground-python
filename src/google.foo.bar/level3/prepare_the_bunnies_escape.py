def solution(maze):
    height, width = get_dim(maze)
    top_to_bottom_path = find_shortest_path(0, 0, maze)
    bottom_to_top_path = find_shortest_path(height - 1, width - 1, maze)

    ans = 2 ** 32 - 1
    for i in range(height):
        for j in range(width):
            if top_to_bottom_path[i][j] and bottom_to_top_path[i][j]:
                ans = min(top_to_bottom_path[i][j] + bottom_to_top_path[i][j] - 1, ans)
    return ans


def get_dim(maze):
    return len(maze), len(maze[0])


def find_shortest_path(start_x, start_y, maze):
    height, width = get_dim(maze)
    board = [[None for _ in range(width)] for _ in range(height)]
    board[start_x][start_y] = 1

    array = [(start_x, start_y)]
    while array:
        x, y = array.pop(0)
        for (x_increment, y_increment) in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + x_increment, y + y_increment
            if 0 <= new_x < height and 0 <= new_y < width:
                if board[new_x][new_y] is None:
                    board[new_x][new_y] = board[x][y] + 1
                    if maze[new_x][new_y] == 1:
                        continue
                    array.append((new_x, new_y))

    return board
