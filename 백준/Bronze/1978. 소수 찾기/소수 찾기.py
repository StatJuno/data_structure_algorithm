N = int(input())
a = list(map(int, input().split()))
k = 0

for i in a:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                k += 1
            break
print(k)
    