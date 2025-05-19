import sys

N = int(input())
l = []
for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    l.append([x,y])

l.sort(key = lambda x: (x[1], x[0]))
for i in l:
    print(i[0], i[1])