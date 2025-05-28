from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

days = [[-1] * m for _ in range(n)]
q= deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i, j))
            days[i][j] = 0
      
### 상하좌우 ###
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

### BFS ###
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 0 and days[nx][ny] == -1:
                grid[nx][ny] = 1
                days[nx][ny] = days[x][y] + 1
                q.append((nx, ny))
                
### Final Result ###
max_day = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(-1)
            exit()
        max_day = max(max_day, days[i][j])

print(max_day)
