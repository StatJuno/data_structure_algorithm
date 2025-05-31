import sys
input = sys.stdin.readline

def backtrack():
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    check = 0
    for i in range(N):
        if not visited[i] and num[i] != check:
            visited[i] = True
            path.append(num[i])
            check = num[i]
            backtrack()
            path.pop()
            visited[i] = False
        
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))

visited = [False] * N
path = []

backtrack()
