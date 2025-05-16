M = int(input())
N = int(input())

l = []
for num in range(M, N+1):
    k = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                k += 1
                break
        if k == 0:
            l.append(num)
            
if len(l) > 0:
    print(sum(l))
    print(min(l))
else:
    print(-1)