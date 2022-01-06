# 프로그래머스 - 금과 은 운반하기
#
# 제한 사항에 제시된 금과 은의 크기 범위를 봤을 때, 이건 이분 탐색이다
# Q. 이 정도의 시간이 주어지면 옮길 수 있는가?
#   - A. 부족하다
#   - A. 충분하다
#   - A. 너무 많다
# 1. 걸릴 수 있는 최대 시간을 구한다.
# 2. 최소로 걸릴 수 있는 시간을 1로 가정한다.
# 3. 그 중간값을 정수로 정한다.
# 4. 중간값의 시간동안 얼마만큼의 금과 은을 옮길 수 있는지 측정한다.
#   Q. 이 정도의 시간이 주어지면 옮길 수 있는가?
#       - A. 부족하다
#       - A. 충분하다
#       - A. 너무 많다


def max_elapsed_time(g, s, w, t):
    max_elapsed = 0
    for i in range(len(g)):
        mineral = g[i] + s[i]
        share = mineral // w[i]
        remainder = mineral % w[i]
        if remainder:
            max_elapsed = max(max_elapsed, (2 * share + 1) * t[i])
        else:
            max_elapsed = max(max_elapsed, (2 * share - 1) * t[i])
    return max_elapsed


def solution(a, b, g, s, w, t):
    start = 0
    # 최대 소요 시간: (한 번에 옮길 수 있는 광물의 양: 1) * (편도로 광물을 한 번 옮기는 시간: 10^5) * (광물의 양: 2*10^9)
    end = max_elapsed_time(g, s, w, t)
    answer = end

    while start <= end:
        mid = (start + end) // 2
        transferred_gold = 0
        transferred_silver = 0
        transferred_mineral = 0

        # 이 중간값의 시간 안에 금과 은을 옮길 수 있는 양을 구하기
        for i in range(len(g)):
            # 1. t[i]와 mid를 사용해 광물을 옮길 수 있는 횟수 구하기 = transferred_count
            share = mid // (2 * t[i])
            remainder = mid % (2 * t[i])
            transferred_count = share + 1 if remainder >= t[i] else share

            # 2. w[i], transferred_count와 g[i], s[i]를 사용해 얼만큼의 금과 은을 옮길 수 있는지 구하기 = transferred_gold, transferred_silver
            transferred_gold += min(transferred_count * w[i], g[i])
            transferred_silver += min(transferred_count * w[i], s[i])

            # 3. w[i], transferred_count와 g[i], s[i]를 사용해 얼만큼의 광물을 옮길 수 있는지 구하기 = transferred_mineral
            transferred_mineral += min(transferred_count * w[i], g[i] + s[i])

        if a <= transferred_gold and b <= transferred_silver and a + b <= transferred_mineral:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer


# 전달해야 하는 광물의 양이 한 번에 옮길 수 있는 광물의 양으로 나누어 떨어지지 않는 경우
assert solution(10, 10, [100], [100], [7], [10]) == 50
# 전달해야 하는 광물의 양이 한 번에 옮길 수 있는 광물의 양으로 나누어 떨어지는 경우
assert solution(10, 10, [100], [100], [10], [10]) == 30
