import sys
N, M = map(int, sys.stdin.readline().split())
basket = [0] * N    
    
for a in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(i, j+1):
        basket[b-1] = k

for i in range(N):
    print(basket[i])

