import sys
from collections import deque
N = int(input())

D = deque()
for i in range(N):
    n = list(map(int, sys.stdin.readline().split()))
    l = len(D)
    if n[0] == 1:
        D.appendleft(n[1])
    elif n[0] == 2:
        D.append(n[1])
    elif n[0] == 3:
        print(D.popleft() if l else -1)
    elif n[0] == 4:
        print(D.pop() if l else -1)
    elif n[0] == 5:
        print(len(D))
    elif n[0] == 6:
        print(0 if l else 1)
    elif n[0] == 7:
        print(D[0] if l else -1)
    elif n[0] == 8:
        print(D[-1] if l else -1)