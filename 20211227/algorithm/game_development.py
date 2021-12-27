directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}


def rotate(current_direction):
    if current_direction == 0:
        return 3
    return current_direction - 1


def one_step(current_location, current_direction, board):
    start_direction = current_direction
    while True:
        next_direction = rotate(current_direction)
        cx, cy = current_location
        nx, ny = cx + directions[next_direction][0], cy + directions[next_direction][1]
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            return (nx, ny), next_direction
        if start_direction == next_direction:
            nx, ny = cx - directions[start_direction][0], cy - directions[start_direction][1]
            if board[nx][ny] == 1:
                return (cx, cy), -1
            return (nx, ny), start_direction
        current_direction = next_direction


def solution(start, direction, board):
    current_direction = direction
    current_location = start
    board[current_location[0]][current_location[1]] = 2
    while current_direction != -1:
        current_location, current_direction = one_step(current_location, current_direction, board)
    cnt = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 2:
                cnt += 1
    return cnt


assert solution((1, 1), 0, [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]) == 3
