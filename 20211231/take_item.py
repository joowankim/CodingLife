# 프로그래머스 - 아이템 줍기
#
# 왼쪽 아래가 (0, 0)
# 도형의 외부에 있는가 내부에 있는가
# 직사각형은 한 변의 길이가 50인 정사각형 내부에 존재한다
# 각 직사각형을 그린다(채워넣는다?) - 외곽선을 추출한다
#   - 직사각형의 외부는 0으로
#   - 직사각형 부분을 1씩 더해서
#   - 1보다 큰 부분을 0으로 만든다
#       - 교점에 대한 처리는?
#           - 외곽선을 추출하면서 교점인지를 파악할 수 있는 방법은 무엇인가?
# 다음 지점으로 갈 수 있는지 판단하는 요소
#   1. 다음 지점이 현재 위치하고 있는 지점의 직사각형 위에 있는 점어야 한다.
#   2. 다음 지점은 직사각형의 외곽선 위에 있는 점이어야 한다.
# 최대 4개의 직사각형을 배치할 수 있다.
# 자료구조는 뭘 쓰지?
#   - 50X50 정사각형을 표현하기 위한 51X51 2차원 리스트 -> 50칸에 여백을 추가한 52칸 정사각형 -> 방향성 체크대신 점을 2배로 찍어서 거리 계산

from collections import deque


def draw_rectangles(rectangles):
    n = 104
    board = [[0] * n for _ in range(n)]

    for lx, ly, rx, ry in rectangles:
        for row in range(2 * ly, 2 * ry + 1):
            for col in range(2 * lx, 2 * rx + 1):
                board[row][col] = 1
    return board


def is_border(picture, x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x + dx, y + dy
            if picture[nx][ny] == 0:
                return True
    return False


def bold_border(picture):
    n = 104
    for row in range(2, n-1):
        for col in range(2, n-1):
            if picture[row][col] == 1 and is_border(picture, row, col):
                picture[row][col] = 2


clockwise = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def route(picture, start, end):
    n = 104
    visited = [[False] * n for _ in range(n)]
    q = deque([(start[1], start[0], 0)])
    visited[start[1]][start[0]] = True
    while q:
        row, col, distance = q.popleft()
        if (col, row) == end:
            return distance//2
        for d_col, d_row in clockwise:
            n_col, n_row = col + d_col, row + d_row
            if not visited[n_row][n_col] and picture[n_row][n_col] == 2:
                visited[n_row][n_col] = True
                q.append((n_row, n_col, distance + 1))


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = draw_rectangles(rectangle)
    bold_border(board)
    distance = route(board, (2 * characterX, 2 * characterY), (2 * itemX, 2 * itemY))
    return distance



assert solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8) == 17
assert solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1) == 11
assert solution([[1, 1, 5, 7]], 1, 1, 4, 7) == 9
assert solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10) == 15
assert solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3) == 10
