T = int(input())
for i in range(T):
    C = int(input())
    for j in [25,10,5,1]:
        print(C // j, end = ' ')
        C %= j