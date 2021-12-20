# 특정 지점을 순회해서 도착하는 최소비용 출력하기
import heapq

INF = int(1e9)


def dijkstra(N, cost_matrix, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = [INF] * N
    distances[start] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if distances[node] < cost:
            continue

        for dst in range(N):
            new_cost = cost + cost_matrix[node][dst]
            if distances[dst] > new_cost:
                distances[dst] = new_cost
                heapq.heappush(pq, (distances[dst], dst))
    return distances


def solution(N, M, edges, X, K):
    costs = [[INF] * N for _ in range(N)]

    # 자기 자신으로 가는 비용 0으로 초기화
    for i in range(N):
        costs[i][i] = 0

    # 양방향 그래프이기 때문에 두 노드가 연결되어 있으면 양쪽으로 가는 비용이 1이 되어야 한다
    for node1, node2 in edges:
        costs[node1-1][node2-1] = 1
        costs[node2-1][node1-1] = 1

    from_1 = dijkstra(N, costs, 0)
    from_k = dijkstra(N, costs, K-1)

    dist = from_1[K-1] + from_k[X-1]

    if dist >= INF:
        return -1
    else:
        return dist


assert solution(5, 7, [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)], 4, 5) == 3
assert solution(4, 2, [(1, 3), (2, 4)], 3, 4) == -1
