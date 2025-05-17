N = int(input())
a = 0

while N >= 0:
    if N % 5 == 0:
        a += int(N // 5)
        print(a)
        break
    
    N -= 3
    a += 1
    
else:
    print(-1)