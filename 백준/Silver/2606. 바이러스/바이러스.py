import sys
input = sys.stdin.readline
N = int(input())
V = int(input())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)

for i in range(V):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v):
    visited[v] = 1
    for x in graph[v]:
        if visited[x] == 0:
            DFS(x)

DFS(1)
print(sum(visited)-1)
    