from collections import deque

def find_brother(N,K):
    max_pos = 100001
    visited = [False] * max_pos
    
    queue = deque()
    queue.append((N,0))
    visited[N] = True
    
    while queue:
        current, time = queue.popleft()
        
        if current == K:
            return time
        
        for next_pos in current-1, current+1, current*2 :
            if 0 <= next_pos < max_pos and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time+1))

N, K = map(int, input().split())
print(find_brother(N, K))