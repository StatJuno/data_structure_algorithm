import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (N+1)

for i in range(N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])