# 특정 지점을 순회해서 도착하는 최소비용 출력하기

INF = int(1e9)


def floyd_warshall(costs):
    N = len(costs)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])


def solution(N, M, edges, X, K):
    costs = [[INF] * N for _ in range(N)]

    # 자기 자신으로 가는 비용 0으로 초기화
    for i in range(N):
        costs[i][i] = 0

    # 양방향 그래프이기 때문에 두 노드가 연결되어 있으면 양쪽으로 가는 비용이 1이 되어야 한다
    for node1, node2 in edges:
        costs[node1-1][node2-1] = 1
        costs[node2-1][node1-1] = 1

    floyd_warshall(costs)

    dist = costs[1][K-1] + costs[K-1][X-1]

    if dist >= INF:
        return -1
    else:
        return dist


assert solution(5, 7, [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)], 4, 5) == 3
assert solution(4, 2, [(1, 3), (2, 4)], 3, 4) == -1
