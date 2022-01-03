# 프로그래머스 - 정수 삼각형
#
# max_values[h][k]: (h+1)층의 (k+1)번째 수가 선택되었을 때의 최대값

def solution(triangle):
    max_values = [[triangle[0][0]]]

    for h in range(1, len(triangle)):
        values = []
        for k in range(len(triangle[h])):
            left = 0
            right = 0
            if 0 < k:
                left = max_values[h-1][k-1]
            if k < len(max_values[h-1]):
                right = max_values[h-1][k]
            values.append(max(left, right) + triangle[h][k])
        max_values.append(values)
    return max(max_values[-1])


assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30
assert solution([[7], [3, 8]]) == 15
