import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = [i for i in range(1, N+1)]
result = []

index = 0
while a:
    index = (index + K - 1) % len(a)
    result.append(a.pop(index))

print("<" + ", ".join(map(str, result)) + ">")
    
