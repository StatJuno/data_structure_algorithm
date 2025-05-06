import sys
N, M = map(int, sys.stdin.readline().split())
basket = list(range(1, N+1))
    
for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    change = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = change

for i in basket:
    print(i, end = ' ')