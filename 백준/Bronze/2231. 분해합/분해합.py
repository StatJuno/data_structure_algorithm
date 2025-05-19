N = int(input())

for i in range(N+1):
    sol = sum(map(int, str(i)))
    sol_sum = i + sol
    
    if sol_sum == N:
        print(i)
        break
    if i == N:
        print(0)
    
    