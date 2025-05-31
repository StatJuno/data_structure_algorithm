import sys
input = sys.stdin.readline

def backtrack(start, path):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    for i in range(start, N+1):
        backtrack(i+1, path + [i])

N, M = map(int, input().split())
backtrack(1, [])