directions = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
]

alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}


def solution(pos):
    cord = list(pos)
    cx, cy = (alphabet[cord[0]], int(cord[1]))
    cnt = 0
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if nx < 1 or nx > 8:
            continue
        if ny < 1 or ny > 8:
            continue
        cnt += 1
    return cnt


assert solution("a1") == 2
