N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_repaint = float('inf')

for i in range(N - 7):
    for j in range(M - 7): 
        repaint1 = 0  # 왼쪽 위가 W인 경우
        repaint2 = 0  # 왼쪽 위가 B인 경우
        for x in range(8):
            for y in range(8):
                curr = board[i + x][j + y]
                if (x + y) % 2 == 0:
                    if curr != 'W': repaint1 += 1
                    if curr != 'B': repaint2 += 1
                else:
                    if curr != 'B': repaint1 += 1
                    if curr != 'W': repaint2 += 1
        min_repaint = min(min_repaint, repaint1, repaint2)

print(min_repaint)