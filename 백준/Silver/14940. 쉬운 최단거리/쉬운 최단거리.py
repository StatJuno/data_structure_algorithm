from collections import deque

n, m = map(int, input().split())
grid = []
visited = [[False] * m for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(m):
        if row[j] == 2:
            start = (i, j)

### BFS 시작 ###            
q = deque()
sx, sy = start
q.append((sx, sy))
visited[sx][sy] = True
distance[sx][sy] = 0

### 상하좌우 ###
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
        
### 최종 결과 ###
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end = ' ')
        elif distance[i][j] == -1:
            print(-1, end = ' ')
        else:
            print(distance[i][j], end = ' ')
    print()
        