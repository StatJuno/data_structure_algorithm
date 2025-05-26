import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, visited, N, M):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    worm_count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y, graph, visited, N, M)
                worm_count += 1
    print(worm_count)