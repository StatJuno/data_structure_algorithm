import sys
N, K = map(int, sys.stdin.readline().split())
a = []
for i in range(1,N+1):
    if N % i == 0:
        a.append(i)
        
print(0) if len(a) < K else print(a[K-1])

    
            
    