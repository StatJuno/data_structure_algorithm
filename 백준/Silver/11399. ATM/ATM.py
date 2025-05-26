N = int(input())
P_i = list(map(int, input().split()))

P_i.sort()
time = 0
total = 0

for i in range(N):
    time += P_i[i]
    total += time
    
print(total)