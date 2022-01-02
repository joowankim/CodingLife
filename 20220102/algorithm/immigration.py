# 프로그래머스 - 입국심사
#
# 심사관마다 심사하는데 걸리는 시간이 다르다
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 반환하기
# - 가장 앞에 서있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있다.
# - 근데, 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있다.
# 시간이 오래 걸린다
# - 심사가 끝날 시간들 중 최소값을 찾는게 비효율적인것 같다.
# - heapq를 사용해도 시간초과가 난다.
# 문제 해결 방법을 보니 한 명씩 배치하는 게 아니다 - 이진 탐색을 사용한다
# 1. 제한시간에서 각 심사대가 몇 명을 처리할 수 있는지 확인한다.
# 2-1. 주어진 명 수보다 많이 처리할 수 있다면 제한 시간을 반으로 나눠 작은 쪽에서 1번을 반복한다.
# 2-2. 주어진 명 수보다 적게 처리할 수 있다면 제한 시간을 반으로 나눠 큰 쪽에서 1번을 반복한다.
# 2-3. 주어진 명 수와 같은 수를 처리할 수 있다면 해당 제한시간을 반환한다.


def solution(n, times):
    limit = max(times) * n

    start = 0
    end = limit
    answer = (start + end)//2

    while start <= end:
        mid = (start + end) // 2
        capacity = 0
        for time in times:
            capacity += mid//time
        if capacity >= n:
            end = mid - 1
            answer = mid
        elif capacity < n:
            start = mid + 1

    return answer


assert solution(1, [10, 9]) == 9
assert solution(6, [7, 10]) == 28
assert solution(6, [3, 10]) == 15
assert solution(6, [3, 9]) == 15
assert solution(6, [3, 1000000000]) == 18
assert solution(1000000000, [1, 1000000000]) == 1000000000
