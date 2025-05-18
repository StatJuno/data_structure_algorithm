import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(N):
    a = int(sys.stdin.readline())
    count[a] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)