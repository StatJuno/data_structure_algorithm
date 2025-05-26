N, M = map(int, input().split())
d = set()
b = set()

for i in range(N):
    d.add(input())
    
for j in range(M):
    b.add(input())

result = sorted(list(d & b))
print(len(result))
for k in result:
    print(k)