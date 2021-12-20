# 전보
import heapq

INF = int(1e9)


def solution(N, aisles, src):
    costs = [INF] * (N + 1)

    # 출발점 비용 초기화
    costs[src] = 0

    matrix = [[INF] * (N+1) for _ in range(N+1)]

    for src, dst, cost in aisles:
        matrix[src][dst] = cost

    pq = []
    heapq.heappush(pq, (costs[src], src))

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_cost > costs[current_node]:
            continue

        for dst in range(N+1):
            new_cost = matrix[current_node][dst] + current_cost
            if costs[dst] > new_cost:
                costs[dst] = new_cost
                heapq.heappush(pq, (costs[dst], dst))

    reachable = list(filter(lambda x: 0 < x < INF, costs))
    return len(reachable), max(reachable)


assert solution(3, [(1, 2, 4), (1, 3, 2)], 1) == (2, 4)
