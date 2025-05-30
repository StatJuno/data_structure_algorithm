import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:    
            print(0)