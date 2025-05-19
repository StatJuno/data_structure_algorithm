from collections import deque
N = int(input())

def p2164(n):
    q = deque(range(1, N+1))
    
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    return q[0]

print(p2164(N))