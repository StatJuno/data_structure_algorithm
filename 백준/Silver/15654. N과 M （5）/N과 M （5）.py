import sys
input = sys.stdin.readline

def backtrack(path, visited):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtrack(path + [l[i]], visited)
            visited[i] = False

N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
visited = [False] * N
backtrack([], visited)