directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}


def solution(N, plan):
    cx, cy = (1, 1)
    for next in plan:
        dx, dy = directions[next]
        nx, ny = cx + dx, cy + dy
        if nx < 1 or N < nx:
            continue
        if ny < 1 or N < ny:
            continue
        cx, cy = nx, ny
    return cx, cy


assert solution(5, ['R', 'R', 'R', 'U', 'D', 'D'])
