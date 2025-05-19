import sys

N = int(input())
l = []
for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    l.append([x,y])

l = sorted(l)
for i in l:
    print(i[0], i[1])