import sys
N = int(input())
l = []
for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    l.append([a,b])

l.sort(key = lambda x: x[0])
for i in l:
    print(i[0], i[1])
