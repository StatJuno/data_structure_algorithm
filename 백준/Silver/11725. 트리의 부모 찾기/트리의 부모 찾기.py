import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
parent = [0] * (N+1)

def dfs(current, prev):
    for neighbor in adj[current]:
        if neighbor != prev:
            parent[neighbor] = current
            dfs(neighbor, current)

dfs(1,0)

for i in range(2, N+1):
    print(parent[i])
    
