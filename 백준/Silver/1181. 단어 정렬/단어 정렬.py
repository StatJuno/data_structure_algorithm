import sys

N = int(input())
l = []

for i in range(N):
    l.append(sys.stdin.readline().strip())

l = list(set(l))
l.sort()
l.sort(key = len)

for i in l:
    print(i)